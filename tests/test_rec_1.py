import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.locator("div").filter(has_text=re.compile(r"^Dashboard$")).click()
    page.get_by_role("listitem").filter(has_text="Nourhann Mab").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.get_by_role("textbox", name="Password").click()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_text("Password", exact=True)).to_be_visible()
    page.get_by_role("textbox", name="Password").click()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.get_by_role("textbox", name="Password")).to_be_empty();
    expect(page.locator("form")).to_contain_text("Password")
