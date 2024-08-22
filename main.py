import time

from playwright.sync_api import Playwright, sync_playwright

from entity.ExcelData import TestDetails, ExcelWorkBook
from service.ExcelControl import StartTest

from service.Browser import *


def run(self: Playwright) -> None:
    # Open Excel WorkBook and create object
    xlwb = ExcelWorkBook("excel\\Test.xlsx", None, None,
                         None, None)

    start = StartTest(self, xlwb)
    start.test_config()

    xlwb.close_workbook()


start_time = time.time()

with sync_playwright() as playwright:
    run(playwright)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
