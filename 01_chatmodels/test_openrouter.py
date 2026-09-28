import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

print("Testing OpenRouter...")


model = init_chat_model(
    "nvidia/nemotron-3.5-lightning:free",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

response = model.invoke(
    "Explain Retrieval Augmented Generation in simple Hinglish."
)

print("\nResponse:")
print(response.content)