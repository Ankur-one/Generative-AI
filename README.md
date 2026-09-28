# 🤖 Free Local AI Chatbot

A completely **free and local AI chatbot** built using **Python, LangChain, Hugging Face Transformers, and TinyLlama**.

This chatbot runs an open-source language model locally on your computer, so it does **not require an OpenAI, Gemini, Mistral, or other paid API key**.

---

## 📌 Project Overview

This project demonstrates how to build a simple conversational AI chatbot using a locally downloaded Large Language Model (LLM).

The chatbot uses:

- 🐍 Python
- 🦜 LangChain
- 🤗 Hugging Face Transformers
- 🧠 TinyLlama 1.1B Chat
- 💬 LangChain ChatHuggingFace
- 🖥️ Local inference

The model is downloaded once and then runs locally.

### Main Flow

```text
                 User
                   │
                   ▼
          ┌─────────────────┐
          │  Chatbot Input  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   LangChain     │
          │ ChatHuggingFace │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ HuggingFace     │
          │    Pipeline     │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   TinyLlama     │
          │    1.1B Chat    │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Generated Reply │
          └────────┬────────┘
                   │
                   ▼
                  User