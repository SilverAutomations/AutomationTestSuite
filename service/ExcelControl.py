import time

from playwright.sync_api import Playwright

from entity.ExcelData import ExcelWorkBook
from service.AssertCode import *
from service.Browser import *
from service.CreateExec import *
from service.ExecuteCode import *
from service.WindowHandler import open_link_in_new_tab_from_element


class StartTest:
    data_dict: dict = {}

    def __init__(self, pw: Playwright, xlwb: ExcelWorkBook):
        self.pw = pw
        self.xlwb = xlwb

    def test_config(self):

        # Change Sheet to Test Details
        self.xlwb.change_sheet(self.xlwb.sheet_names.index("Details"))

        # Create Object for test Details
        td = TestDetails(self.xlwb)

        print(f"WorkBook Sheets: {self.xlwb.sheet_names}  ({self.xlwb.sheet_count})")

        # Create Playwright objects for browser, browser-context and page
        browser = select_browser(self.pw, td.browser, td.headless, td.cdp)
        context = open_browser_context(browser, td.cdp)
        page = open_page(context, td.cdp)

        url = td.website
        page.goto(url)

        for i in range(0, self.xlwb.sheet_count):
            if "test" in self.xlwb.sheet_names[i].lower():
                self.xlwb.change_sheet(i)
                self.test_sheets(page, self.xlwb.sheet_names[i])

        close_page(page)
        close_browser_context(context)
        close_browser(browser)

    def test_sheets(self, page: Page, sheet_name: str):
        print("Current testing: " + sheet_name)

        exec_str: str

        # Traversing through each row one by one and creating objects for each row
        for row in range(2, self.xlwb.get_rows_count()):
            tr = TestRow(self.xlwb, row)
            if "start loop" in tr.description:
                print(f"Running loop: {tr.description}")
                row = self.loop_cases_element(page, row, tr.locator, tr)
            elif tr.execute != "":
                exec_str = tr.execute
                print(exec_str)
            else:
                if "hard" in tr.assertion.lower():
                    hard_assert(self.pw, page, tr)
                elif "soft" in tr.assertion.lower():
                    soft_assert(self.pw, page, tr)
                exec_str = create_exec_str(tr, None)
                print(exec_str)
                if tr.storedvaluekey != "":
                    self.data_dict[tr.storedvaluekey] = execute_code_data(self.pw, page, exec_str)
                else:
                    execute_code(self.pw, page, exec_str)
        print(self.data_dict)

    def loop_cases_element(self, page: Page, row: int, loop_locator: str, tr: TestRow) -> int:

        if "hard" in tr.assertion:
            hard_assert(self.pw, page, tr)
        elif "soft" in tr.assertion:
            soft_assert(self.pw, page, tr)

        # Get the element list from the locator in start loop row
        exec_str = create_exec_str(tr, None)
        execute_code(self.pw, page, exec_str)
        print(exec_str)
        element_list: list = page.locator(tr.locator).all()
        print(len(element_list))

        temp_row = row  # 5-7

        for element in element_list:
            temp_row = row
            tr = TestRow(self.xlwb, temp_row)
            while "end loop" not in tr.description:
                if "start loop" in tr.description:
                    temp_row = self.loop_cases_element(page, temp_row, tr.locator, tr)
                elif tr.execute != "":
                    exec_str = tr.execute
                    print(exec_str)
                else:
                    if "hard" in tr.assertion.lower():
                        hard_assert(self.pw, page, tr)
                    elif "soft" in tr.assertion.lower():
                        soft_assert(self.pw, page, tr)
                    exec_str = create_exec_str(tr, element)
                    print(exec_str)
                    if tr.storedvaluekey != "":
                        self.data_dict[tr.storedvaluekey] = execute_code_data(self.pw, page, exec_str)
                    else:
                        execute_code(self.pw, page, exec_str)

                temp_row = temp_row + 1
                tr = TestRow(self.xlwb, temp_row)

        row = temp_row
        return ++row
