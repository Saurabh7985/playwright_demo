import re
from playwright.sync_api import Page, expect




def test_example(page: Page) -> None:
    page.goto("https://www.flipkart.com/")
    page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox").click()
    page.get_by_role("button", name="✕").click()
    page.get_by_role("link", name="Electronics").click()
    expect(page.get_by_role("link", name="Grooming")).to_be_visible()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Drinkware").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="₹367 ₹1,398 73% off").click()
    page1 = page1_info.value
    page1.locator("._1psv1zeb9._1psv1ze0._7dzyg20 > ._1psv1zeb9._1psv1ze0._1o6mltljp._1o6mltler._1o6mltl4v._1o6mltl9t._7dzyg24v").first.click()
