try:
    from dotenv import load_dotenv
except ModuleNotFoundError as exc:
    if exc.name != "dotenv":
        raise
    raise RuntimeError(
        "Missing dependency: install it in the active Python environment with "
        "`python -m pip install python-dotenv`, then select that "
        "environment as your editor's Python interpreter."
    ) from exc

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ModuleNotFoundError as exc:
    if exc.name != "langchain_google_genai":
        raise
    raise RuntimeError(
        "Missing dependency: install it in the active Python environment with "
        "`python -m pip install langchain-google-genai`, then select that "
        "environment as your editor's Python interpreter."
    ) from exc

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

response = model.invoke(
    "Explain LangChain in simple Hinglish."
)

print(response.content)