import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(self: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")

    page.get_by_title("Search in").select_option("search-alias=electronics")
    page.locator("//input[@id='twotabsearchtextbox']").fill("Camera")
    page.locator("//input[@id='nav-search-submit-button']").click()

    time.sleep(5)

    elements = page.locator(
        "//*[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").all()
    child_links = [element.get_attribute("href") for element in elements]
    print(len(child_links))
    for link in child_links:
        print(link)

    i: int = 0
    for cl in child_links:
        new_window = page.context.new_page()
        # new_window.wait_for_load_state("domcontentloaded")
        new_window.goto("https://www.amazon.in" + child_links[i])
        i = i + 1
        new_window.bring_to_front()
        print(new_window.wait_for_selector("#productTitle", timeout=30000).text_content().strip())
        new_window.close()

    # open_pages = context.pages
    # print(len(open_pages))
    # for p in open_pages:
    #     print(p)

    # page.wait_for_selector("//*[@id='productTitle'").text_content()
    #
    # time.sleep(5)
    #
    # # open_pages = context.pages
    # # print(len(open_pages))
    # # for p in open_pages:
    # #     print(p)
    # #
    # # time.sleep(5)
    #
    # page.wait_for_selector("//*[@id='productTitle'").text_content()
    # # page.locator("//*[@id='productTitle'").text_content()
    # page.locator("//span[normalize-space()='Show More']").click()
    # page.locator("//ul[@class='a-unordered-list a-vertical a-spacing-mini']").text_content()

    # elements = page.locator("//*[@class='a-size-medium a-color-base a-text-normal']").all()
    #
    # print(len(elements))
    #
    # for element in elements:
    #     txt = element.text_content()
    #     print(txt)

    time.sleep(5)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
