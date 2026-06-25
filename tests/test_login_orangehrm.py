import re
from playwright.sync_api import Page 
from pages.orange_login_page import LoginPage
from pages.oranghrm_home_page import  HomePage





def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    Home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.login("Admin","admin123")
    print("current Url:",page.url)
    page.screenshot(path="debug.png")
    print(page.content())
    Home_page.homep()

    
    

