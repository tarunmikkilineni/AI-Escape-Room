
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found. Check your .env file.")
else:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model="gemini-4-hydrogen",    
    contents="Say hello to the player of my mysterious library escape room."
    )

    print(response.text)
