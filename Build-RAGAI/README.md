# Build-RAGAI

## Description
This project seeks to teach you how to build Python applications with generative AI functionality by using the LangChain and Transformers libraries.

While there is a section for [OpenAI](./src/opai/), most of the code that previously existed there has been repurposed and integrated with either the [LangChain](./src/langchain/) or [Transformers](./src/transformers/) libraries. This project includes code snippets, end2end examples, and jupyter notebooks that you can augment, copy, or learn from respectively.

If you're new to building AI-powered applications, I suggest you start by playing with and executing the code in the [LangChain notebooks](./src/langchain/notebooks/). Seeing the code in action, editing it yourself, and creatively brainstorming new ideas is the best way to learn.

## Table of Contents
Below you'll find links to, and descriptions of, sections of this project for easy navigation.

This README:
- [Getting Started](#getting-started)
- [Installation](#installation)
- [License](#license)

LangChain:
- [Code Snippets](./src/langchain/codesnippets/ "Directory"): Here you'll find pluggable Python components.
  - [bufferwindow_memory.py](./src/langchain/codesnippets/bufferwindow_memory.py "Code Snippet"): A simple memory component that can be used in a LangChain conversation.
  - [chatopenai.py](./src/langchain/codesnippets/chatopenai.py "Code Snippet"): A simple LLM component that can be used to return chat messages.
  - [multi_queryvector_retrieval.py](./src/langchain/codesnippets/multi_queryvector_retrieval.py "Code Snippet"): An advancced retriever component that combines the power of multi-querying and multi-vector retrieval.
- [End to End Examples](./src/langchain/end2end/ "Directory"): Here you'll find scripts made to work out of the box.
  - [RAG with Agents](./src/langchain/end2end/rag-with-agents/ "Directory"): Learn to use Agents for RAG.
    - [Streamlit Chatbot](./src/langchain/end2end/chatbots/streamlit/ "Directory"): A simple Streamlit chatbot using OpenAI.
    - [Directory Loader](./src/langchain/end2end/rag-with-agents/directoryloader/README.md "Directory"): Use the `DirectoryLoader` class to load files for querying.
    - [PyPDF Directory Loader](./src/langchain/end2end/rag-with-agents/pypdfdirectoryloader/README.md "Directory"): Use the `PypdfDirectoryLoader` class to load files for querying.
    - [Facebook AI Similarity Search](./src/langchain/end2end/rag-with-agents/faiss_retriever.py "Directory"): Use the `FacebookAISimilaritySearch` class to load files for querying.
  - [Using Tools](./src/langchain/end2end/usingtools/ "Directory"): Learn how to use tools in LangChain.
    - [Image Generation and Captioning](./src/langchain/end2end/usingtools/image_generation_and_captioning.ipynb "Jupyter Notebook"): Practice using HuggingFace's "Spaces" as a tool for an Agent Executor.
    - [OpenAI Functions Parser](./src/langchain/end2end/usingtools/openai_functionsparser_serpsearching.ipynb "Jupyter Notebook"): Practice using two LangChain-native tools: "serpapi" and "llm-math" via OpenAI function calling and implementing the `OpenAIFunctionsAgentOutputParser`.
  - [Vectorstore RAG](./src/langchain/end2end/vectorstore-rag/ "Directory"): Learn how to use vectorstores in LangChain.
    - [Pinecone](./src/langchain/end2end/vectorstore-rag/pinecone/README.md "Directory"): Use a `Pinecone` vector database "Index" as a retriever and chat with your documents. 

---

## Getting Started

### Installation

#### Local Code Execution and Testing
This project is developed using [PDM](https://pdm.fming.dev/). I recommend you install and use PDM to ensure you're taking steps that have already been tested and verified as working correctly. You can install PDM using `pip`:

Start by navigating to the root directory of this project.

```bash
pip install -U pdm
```

Then you'll need to install the dependencies using PDM:

```bash
pdm install
```

This command will create a virtual environment in `.venv` and install the dependencies in that environment. If you're on macOS or Linux, you can run `source .venv/bin/activate` to activate the environment. Otherwise, you can run the command `.venv/Scripts/activate` or `.venv/Scripts/activate.ps1` to activate the environment.

By using a virtual environment we avoid cross contaminating our global Python environment.

Once our virtual environment is set up we need to select it as our kernel for the Jupyter Notebook. If you're in VSCode, you can do this at the top right of the notebook. If you're using a different IDE, you'll need to look for setup help online.

When selecting the kernel, ensure you choose the one that's located inside of the `.venv` directory, and not the global Python environment.

#### Google Colab Execution and Testing

To get started in Google Colab, you can upload any of the notebooks from this repository, OR click the badge below to open the [starter LangChain RAG notebook](./src/langchain/notebooks/learn_rag.ipynb "Starter RAG Notebook for learning") in Colab.

<a target="_blank" href="https://colab.research.google.com/github/Daethyra/Build-RAGAI/blob/master/src/langchain/notebooks/learn_rag.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open 'learn_rag.ipynb' In Colab"/>
</a>

---

## [LICENSE](./LICENSE "GNU Affero GPL")
