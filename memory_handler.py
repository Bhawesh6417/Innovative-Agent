# This will act as our custom memory
chat_history = []

def add_to_history(role, content):
    chat_history.append({"role": role, "content": content})

def get_history_text():
    return "\n".join([f"{item['role'].capitalize()}: {item['content']}" for item in chat_history])

# Session flag to track whether we're refining an idea
idea_session_active = False

def activate_idea_session():
    global idea_session_active
    idea_session_active = True

def is_idea_session_active():
    return idea_session_active

def extract_fields_for_idea():
    """Heuristically extract structured idea info from chat history"""
    user_responses = [msg["content"] for msg in chat_history if msg["role"] == "user"]
    assistant_responses = [msg["content"] for msg in chat_history if msg["role"] == "assistant"]

    return {
        "title": user_responses[0][:50] if user_responses else "Untitled Idea",
        "abstract": assistant_responses[0] if assistant_responses else "",
        "problemStatement": user_responses[1] if len(user_responses) > 1 else "Problem not specified",
        "solutionSummary": assistant_responses[-1] if assistant_responses else "",
        "createdBy": "bhawesh@example.com",  # or replace with actual user system
        "areaOfImpact": ["Healthcare"],
        "isNewIdea": True,
        "innovationStage": "Idea",
        "relatedTechnologies": ["AI", "Computer Vision"],
        "impactMetrics": {"surgical_error_reduction": "20%", "time_saved": "15 mins/case"},
        "votes / likes": 0,
        "feedbackHistory": assistant_responses
    }
