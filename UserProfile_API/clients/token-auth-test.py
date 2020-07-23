import requests

def client():
    credentials = {"username" : "sagar", "password" : "shyamshyam10"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                            data = credentials)

    print("status code:", response.status_code)
    #response_data = response.json()
    print(response)


if __name__ =="__main__":
    client()