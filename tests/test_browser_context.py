from playwright.sync_api import Page

from pages.orange_login_page import LoginPage



def test_three_user(browser):
    admin_context=browser.new_context()
    admin_page=admin_context.new_page()

    user1_context=browser.new_context()
    user1_page=user1_context.new_page()

    user2_context=browser.new_context()
    user2_page=user2_context.new_page()

    admin=LoginPage(admin_page)
    user1=LoginPage(user1_page)
    user2=LoginPage(user2_page)

    admin.login("Admin","admin123")
    user1.login("Admin","admin123")
    user2.login("Admin","admin123")



