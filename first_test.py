import time
from playwright.sync_api import Page

# with sync_playwright() as p:
#     # Launch the browser. Set headless=False to physically open the window.
#     # You can change 'chromium' to 'firefox' or 'webkit'
#     browser = p.chromium.launch(headless=False)
    
#     # Create a new pristine browser page/tab
#     page = browser.new_page()
def browser(page):
    
    # Navigate to a specific website
    page.goto("https://flipkart.com")
    
    # Optional: Print the title to verify it worked
    print(f"Page Title: {page.title()}")
    
    # Keep the browser open for 5 seconds so you can see it
    time.sleep(15)
    
    # Close the browser session gracefully
    
