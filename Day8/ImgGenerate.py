import requests
from pprint import pprint
import base64#Base64 encodes arbitrary binary data into a restricted set of ASCII characters,
# which are represented as bytes (binary) during transmission.
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("api")

url = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {
    "Authorization": f"Bearer {api_key}",

    
}

data = {
    "inputs": "A cyberpunk city at night"
}

response = requests.post(url, headers=headers, json=data)

print("status_code:", response.status_code)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("Image saved as ouput.png")
else:
    print(response.text)