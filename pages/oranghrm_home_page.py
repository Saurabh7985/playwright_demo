from playwright.sync_api import Page,expect

class HomePage:
    def __init__ (self,page:Page):
        self.page=page
        self.upgrade_button=page.get_by_role("button", name="Upgrade")
        self.performance_link=page.get_by_role("link", name="Performance")
        self.dashboard_link=page.get_by_text("Dashboard")      
        self.Logout_button=page.get_by_role("button",name="logout")

    def upgrade_visible(self):
        expect(self.upgrade_button).to_be_visible()

    def click_perfomance(self):
        self.performance_link.click()

    def click_dashboard(self):
        self.dashboard_link.click()

    def click_logout(self):
        self.Logout_button.click()
    
    def homep(self):
        self.click_dashboard()
        self.click_perfomance()
        self.click_logout()


