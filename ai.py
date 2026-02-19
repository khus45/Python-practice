from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize client (it will automatically pick OPENAI_API_KEY from .env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5.2",
    input="tell me about gaya city in bihar in 100 words"
)

print(response.output_text)