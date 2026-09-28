from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

# Load API keys from .env
load_dotenv()

question = "Explain RAG in simple Hinglish."


# =========================
# Gemini
# =========================

print("=" * 50)
print("GEMINI")
print("=" * 50)

try:
    gemini = init_chat_model(
        "gemini-3.8-flash",
        model_provider="google_genai"
    )

    response = gemini.invoke(question)

    print(response.content)

except Exception as e:
    print("Gemini Error:")
    print(e)


# =========================
# OpenRouter - Nemotron
# =========================

print("\n" + "=" * 50)
print("OPENROUTER - NEMOTRON")
print("=" * 50)

try:
    nemotron = init_chat_model(
        "nvidia/llama-3.1-nemotron-ultra-253b-v1",
        model_provider="openai",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    response = nemotron.invoke(question)

    print(response.content)

except Exception as e:
    print("Nemotron Error:")
    print(e)