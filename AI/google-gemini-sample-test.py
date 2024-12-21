import google.generativeai as genai
import os

# Replace 'your-gemini-api-key' with your actual API key
API_KEY = "AIzaSyDQB7Rq80f69wT0ZtNOBgvsuFCs94f7KnA"

# Configure the Gemini API key
genai.configure(api_key=API_KEY)

# Sample prompt to test the API
prompt = "What is Gemini AI?"

# Generate response using Chat API (Google's Gemini models)
response = genai.chat(model="gemini", messages=[{"role": "user", "content": prompt}])

# Print the response
print("Response:", response["messages"][0]["content"])