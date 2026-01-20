import requests
import pandas as pd
import pprint 
from dotenv import load_dotenv
import os
load_dotenv()
city="Kathmandu"
api_key=os.getenv("API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    pprint.pprint(data)
else:
    print("status code: ",response.status_code)
