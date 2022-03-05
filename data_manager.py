from urllib import response
import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL_SHEETY=os.getenv("URL_SHEETY")
BEARER_SECRET=os.getenv("BEARER_SECRET")

bearer_header={
    "Authorization":BEARER_SECRET
}

class DataManager:
    def __init__(self):
        self.destination_data={}
    
    def get_destination_data(self):
        response=requests.get(url=URL_SHEETY,headers=bearer_header)
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_code={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            reponse=requests.put(url=f"{URL_SHEETY}/{city['id']}",json=new_code,headers=bearer_header)
            print(reponse.text)