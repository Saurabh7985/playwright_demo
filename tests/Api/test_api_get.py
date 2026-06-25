#for get request
def test_api_get(playwright):
    request=playwright.request.new_context()
    response=request.get("https://restful-booker.herokuapp.com/booking")
    assert response.status ==200
    json_data=response.json()
    print(json_data)
    request.dispose()
    print("test Completed suceesfully")

#for creating token

def create_token(playwright):
    request=playwright.request.new_context()
    response=request.post("https://restful-booker.herokuapp.com/auth",data={
        "username":"admin",
        "password":"password123"
    })
    # return response.jason()["token"]
    assert response.status ==200
    json_data=response.json()
    print(json_data)
    request.dispose()
    print("test Completed suceesfully")
    
    


