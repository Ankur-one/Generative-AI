from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


# Load local LLM
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 256,
        "do_sample": False,
        "repetition_penalty": 1.03,
    },
)


# Convert LLM into chat model
chat_model = ChatHuggingFace(llm=llm)


print("===================================")
print("       FREE LOCAL AI CHATBOT")
print("===================================")
print("Type 'exit' to stop.\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chat_model.invoke(user_input)

    print("Bot:", response.content)
    print()