import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL_SHEETY=os.getenv("URL_SHEETY")
BEARER_SECRET=os.getenv("BEARER_SECRET")

bearer_header={
    "Authorization":BEARER_SECRET
}

excel_peticion = requests.get(url=URL_SHEETY, headers=bearer_header)

print(excel_peticion.text)