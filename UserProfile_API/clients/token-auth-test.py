import requests

def client():
    token_h = "Token e2537daa720cc3814109ba692e76b7e2cac5a1ed"
   
    #credentials = {"username" : "shyam", "password" : "shyam"}
    #response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",data=credentials)
    headers = {"Authorization" : token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("status code:", response.status_code)
    response_data = response.json()
    print(response_data)
    for profile in response_data:
        print(f"{profile['id']} -----> {profile['user']}")

if __name__ == "__main__":
    client()