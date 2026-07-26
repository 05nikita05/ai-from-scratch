import os
import urllib.request
import json
from dotenv import load_dotenv
from requests import HTTPError

load_dotenv()  # reads .env and loads variables into environment

# url = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" 
# "https://googleapis.com"

api_key = os.environ.get("GEMINI_API_KEY")
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key 
}

body = json.dumps({

     "contents": [
        {
            "role": "user",
            "parts": [{"text": "What is a neural network in one sentence?"}]
        }
    ]
}).encode("utf-8")

req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
        # FIXED: Access the list index [0] before accessing key ["text"]
        print((result["candidates"][0]["content"]["parts"][0]["text"]))
except Exception as e:
    print(e)