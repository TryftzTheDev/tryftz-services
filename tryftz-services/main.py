import requests
import time

# ⚠️ Replace this with your real Discord user token
TOKEN = "your_discord_user_token"

# Replace with the channel ID you want to send the message to
CHANNEL_ID = "123456789012345678"

# Your repeated message
MESSAGE = "This is my repeated message."

# How often to send the message (in seconds)
INTERVAL = 60

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

payload = {
    "content": MESSAGE
}

while True:
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200 or response.status_code == 204:
        print("Message sent.")
    else:
        print(f"Failed to send: {response.status_code} - {response.text}")
    time.sleep(INTERVAL)