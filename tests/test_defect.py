import re
from playwright.sync_api import sync_playwright,Page



def run(page:Page,browser,context) -> None:

    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    page.goto("https://tourmaline-monstera-c13fae.netlify.app/index.html")
    page.get_by_role("textbox", name="Username *").click()
    page.get_by_role("textbox", name="Username *").fill("a")
    page.get_by_role("textbox", name="Password *").click()
    page.get_by_role("textbox", name="Password *").fill("a")
    page.get_by_role("textbox", name="Password *").press("Enter")


    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
