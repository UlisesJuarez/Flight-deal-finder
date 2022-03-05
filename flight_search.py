import code
from email import header
from unittest import result
import requests
import os
from dotenv import load_dotenv
load_dotenv()
TEQUILA_ENDPOINT =os.getenv("TEQUILA_ENDPOINT")
TEQUILA_API_KEY =os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    
    def get_destination_code(self,city_name):
        location_endpoint=f"{TEQUILA_ENDPOINT}/locations/query"
        headers={"apiKey":TEQUILA_API_KEY}
        query={"term":city_name,"location_types":"city"}
        response=requests.get(url=location_endpoint,headers=headers,params=query)
        result=response.json()["locations"]
        code=result[0]["code"]
        return code