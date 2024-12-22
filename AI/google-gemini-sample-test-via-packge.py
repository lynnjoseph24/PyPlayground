import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API key is missing! Check the .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the prompt
prompt = "Explain how AI works"

# Generate response
response = model.generate_content(prompt)

# Print the response
print("Response:", response.text)