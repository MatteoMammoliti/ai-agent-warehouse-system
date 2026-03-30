# 📦 Intelligent Warehouse Agent
### *A Multi-Agent System for Smart Inventory Management*

[![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-ace1af?style=for-the-badge&logo=chainlink)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/Orchestrated%20by-LangGraph-orange?style=for-the-badge&logo=diagram&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Model](https://img.shields.io/badge/Model-Llama--3.3--70B-blueviolet?style=for-the-badge)](https://groq.com/)

A simple AI-driven warehouse assistant that utilizes **LangGraph** to orchestrate a state-based workflow for inventory queries, supplier documentation analysis, and real-time stock monitoring.

## 🚀 Overview

This project implements a **Conditional State Machine** for warehouse management. The agent goes beyond simple text retrieval by reasoning about user intent, validating entities through a normalization layer, and dynamically constructing SQL queries to provide precise, real-time stock data.

## 🛠️ Tech Stack

* **Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/)
* **LLM Framework:** [LangChain](https://python.langchain.com/)
* **Inference Engine:** [Groq Cloud](https://groq.com/)
* **Model:** Llama-3.3-70B-Versatile
* **Database:** SQLite3
* **Validation:** Pydantic (Structured Output)

## 📁 Project Structure

```text
├── chains/               # Specialized LLM chains (Router, Validator, Generator)
├── nodes/                # Python logic for each Graph state node
├── schemas/              # Pydantic models & GraphState definition
├── magazzino.db          # SQLite Database
├── graph.py              # Main LangGraph orchestration & Graph compilation
└── output.png            # Mermaid diagram of the compiled graph
```

Developed with ❤️ using Python, LangGraph and Llama 3.
