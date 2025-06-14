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



