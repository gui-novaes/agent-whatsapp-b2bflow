import requests
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN_ZAPI = os.getenv("CLIENT_TOKEN_ZAPI")

print(SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE_ID, ZAPI_TOKEN)

# Conect Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Search pending messages
def search_messages():
    response = supabase.table("messages").select("*").eq("status", "pendente").execute()
    return response.data

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
    #Aqui está o erro
    print("URL: ", url)
    print("Payload: ", payload)
    print("Response: ", response.text)
    print("Status Code: ", response.status_code)
    return response

# Update status with Supabase
def update_status(id, status):
    supabase.table("messages").update({"status": status}).eq("id", id).execute()

# Main logic 
# Send messages using Supabase database
messages = search_messages()

for msg in messages:
    success = send_messages(msg["phone"], msg["message"])
    if success:
        update_status(msg["id"], "enviado")
        print(f"✅ Mensagem enviada com sucesso para {msg['name']}, número: {msg['phone']}")
    else:
        update_status(msg["id"], "erro")
        print(f"❌ Falha ao enviar mensagem para {msg['name']}, número: {msg['phone']}")
