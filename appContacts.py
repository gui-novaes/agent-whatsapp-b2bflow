import time
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN_ZAPI = os.getenv("CLIENT_TOKEN_ZAPI")

# Send messages with Zapi
def send_messages(number, text):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    headers = {
        "Content-Type": "application/json",
        "Client-Token": f"{CLIENT_TOKEN_ZAPI}"
    }

    payload = {
        "phone": number,
        "message": text
    }
    
    response = requests.post(url, json=payload, headers=headers)

    print("URL: ", url)
    print("Payload: ", payload)
    print("Response: ", response.text)
    print("Status Code: ", response.status_code)
    return response

# Contact list for sending automatic messages
contacts = [
    {"name": "Marcelo", "phone": "5511940804809"},
    {"name": "Guilherme", "phone": "5511991421839"},
]

# Loop to send the messages
for contact in contacts:
    message = f"Olá {contact['name']}, tudo bem? Essa é uma mensagem automática do código do Guilherme"
    send_messages(contact["phone"], message)
    time.sleep(2)