import re
import pytest

from playwright.sync_api import Page, expect
import csv
def get_csv():
    data=[]
    with open("test_data/data.csv") as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data   
import json
def get_json():
    with open("test_data/data.json") as file:
        data=json.load(file)
    return [
        [item["username"],
         item["password"]]
                              for item in data
    ]
        
     
@pytest.mark.parametrize("username,password",get_json())
# @pytest.mark.parametrize("username,password",[
#     ("Admin","admin123"),
#     ("user1","password1"),
#     ("user2","password2")
# ])
def test_example(page: Page,username,password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
