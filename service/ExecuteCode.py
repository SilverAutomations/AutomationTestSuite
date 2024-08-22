import time

from playwright.sync_api import Playwright, sync_playwright, Page


def execute_code(pw: Playwright, page: Page, exec_str: str):
    # page.wait_for_load_state('networkidle')
    return exec(exec_str)


def execute_code_data(pw: Playwright, page: Page, exec_str: str):
    return exec(exec_str)


def execute_code_window_handler(pw: Playwright, page: Page, code: str):
    """

    :param pw:
    :param page:
    :param code:
    :return:
    """
