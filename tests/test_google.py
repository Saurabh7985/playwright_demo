import re 
from playwright.sync_api import expect


def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button",name="Accept all").click(timeout=5000)
    except:
        print("No popup for accept")
    page.get_by_role("combobox",name="search").fill("playwright Python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("playwright",re.IGNORECASE))
