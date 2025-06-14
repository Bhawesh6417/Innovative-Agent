from langchain_core.prompts import PromptTemplate

idea_prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
You are an AI assistant helping users turn ideas into innovation proposals.

Conversation history:
{chat_history}

Current user input:
{user_input}

Ask smart follow-up questions and try to collect info like:
- Target audience
- Domain
- Technologies
- Proposal details

Respond:"""
)
