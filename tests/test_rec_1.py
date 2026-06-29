import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Performance")).to_be_visible()
    page.get_by_role("link", name="Recruitment").click()
    page.get_by_role("link", name="Maintenance").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    page.get_by_role("link", name="Dashboard").click()
    page.get_by_role("listitem").filter(has_text="jhon use&r").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()






