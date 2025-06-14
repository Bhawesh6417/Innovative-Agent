# Innovation Agent Chatbot

A multi-turn conversational AI assistant that helps users refine innovation ideas using LangChain and Groq LLMs — then exports them as structured JSON compliant with your Innovation DB schema.

---

## Features

**Query Router**: Automatically detects if user input is:
  - A new innovation idea
  - A request to search the Innovation DB
  - A MedTech-related question
  - Irrelevant

**Multi-Turn Memory**: Tracks user responses across multiple messages to help refine an idea step-by-step.

**Schema-Compliant JSON Export**: When the user types `submit`, the conversation is saved as a structured innovation idea with fields like:
  - `ideaId`, `title`, `problemStatement`, `areaOfImpact`, `innovationStage`, etc.

**Groq API Powered**: Uses `llama3-8b-8192` from Groq's OpenAI-compatible endpoint for fast and affordable responses.


## 📁 Folder Structure

  innovation_agent/
  ├── app.py # Main loop for user input and routing
  ├── router.py # Classifies user queries
  ├── memory_handler.py # Tracks chat history and idea session flag
  ├── prompt_templates.py # Defines prompt structure
  ├── groq_wrapper.py # Handles LLM API calls to Groq
  ├── db_handler.py # Placeholder for Innovation DB queries
  ├── .env # Secure API and credential config
  └── requirements.txt # Python dependencies

