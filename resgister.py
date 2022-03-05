import os
import re
from unittest import result
import requests
from dotenv import load_dotenv

load_dotenv()

URL_SHEETY_USERS = os.getenv("URL_SHEETY_USERS")
BEARER_SECRET = os.getenv("BEARER_SECRET")

bearer_header = {
    "Authorization": BEARER_SECRET
}

new_user = {
    "user": {
        "firstName":input("What is your first name: "),
        "lastName":input("What is your last name: "),
        "email":input("What is yout email: ")
    }
}



response=requests.post(url=URL_SHEETY_USERS,headers=bearer_header,json=new_user)

dato=requests.get(url=URL_SHEETY_USERS,headers=bearer_header)
print(dato.text)