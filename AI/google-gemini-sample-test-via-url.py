import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API key is missing! Check the .env file.")

# Gemini API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Headers
headers = {
    "Content-Type": "application/json"
}

# Request data
data = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

# Make POST request
response = requests.post(url, headers=headers, json=data)

# Check response status
if response.status_code == 200:
    # Parse JSON response
    result = response.json()
    # Extract and print the response
    print("Response:", result['candidates'][0]['content']['parts'][0]['text'])
else:
    print(f"Error {response.status_code}: {response.text}")