from dotenv import load_dotenv
from importlib import import_module

try:
    ChatMistralAI = import_module("langchain_mistralai").ChatMistralAI
except ModuleNotFoundError as exc:
    if exc.name == "langchain_mistralai":
        raise ImportError(
            "Install the integration with `python -m pip install langchain-mistralai`."
        ) from exc
    raise

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

response = model.invoke(
    "Explain LangChain in simple Hinglish."
)

print(response.content)