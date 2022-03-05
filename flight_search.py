import code
import requests
import os
from dotenv import load_dotenv
load_dotenv()
TEQUILA_ENDPOINT =os.getenv("TEQUILA_ENDPOINT")
TEQUILA_API_KEY =os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    
    def get_destination_code(self,city_name):
        code="TESTING"
        return code