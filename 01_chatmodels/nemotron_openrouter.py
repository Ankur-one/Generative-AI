import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Ask Nemotron
response = client.chat.completions.create(
    model="nvidia/nemotron-3.5-lightning",
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in simple Hinglish."
        }
    ],
)

# Print answer
print(response.choices[0].message.content)