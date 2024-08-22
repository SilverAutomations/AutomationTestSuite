from playwright.sync_api import Page, Playwright, BrowserContext
from selenium import webdriver

from entity.ExcelData import TestRow


def open_url_in_new_window(pw: Playwright, page: Page, url: str):
    new_window = page.context.new_page()
    new_window.goto(url)
    new_window.bring_to_front()
    return page


def open_link_in_new_tab_from_element(pw: Playwright, page: Page, element):
    all_before = page.context.pages
    all_after = all_before
    element.click()
    temp_page = page.context.new_page()
    temp_page.goto("https://www.google.com")

    while len(all_after) <= (len(all_before) + 1):
        all_after = page.context.pages

    for af in all_after:
        print(af.title())
        af.bring_to_front()

    temp_page.close()




def goto_parent_window(pw: Playwright, page: Page):
    total_pages = page.context.pages
    total_pages[0].bring_to_front()
    return page
