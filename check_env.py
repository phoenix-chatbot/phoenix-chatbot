from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
