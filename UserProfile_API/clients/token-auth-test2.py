import requests

def client():
    #token_h = "Token e2537daa720cc3814109ba692e76b7e2cac5a1ed"
   
    data = {
                    "username" : "hardik", 
                    "email":"shyam@django.com",
                    "password1" : "asdf123123",
                    "password2": "asdf123123",
                    }
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration", 
                            data=data)
    #headers = {"Authorization" : token_h}

   # response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("status code:", response.status_code)
    response_data = response.json()
    
    print(response_data)
    # for profile in response_data:
    #     print(f"{profile['id']} -----> {profile['user']}")

if __name__ == "__main__":
    client()