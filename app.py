from dotenv import load_dotenv
import os
import json
import uuid
from datetime import datetime
from router import route_query
from prompt_templates import idea_prompt
from memory_handler import (
    add_to_history, get_history_text,
    activate_idea_session, is_idea_session_active,
    extract_fields_for_idea
)
from db_handler import query_db
from groq_wrapper import get_groq_llm_response

load_dotenv()

def handle_query(user_input):
    if user_input.lower() == "submit":
        fields = extract_fields_for_idea()
        return export_idea_to_json(fields)

    add_to_history("user", user_input)
    category = route_query(user_input)

    if is_idea_session_active():
        category = "IDEA"

    if category == "IDEA":
        activate_idea_session()
        history = get_history_text()
        full_prompt = idea_prompt.format(chat_history=history, user_input=user_input)
        response = get_groq_llm_response(full_prompt)
        add_to_history("assistant", response)
        return response

    elif category == "DB":
        return query_db(user_input)

    elif category == "MEDTECH":
        return "As this is MedTech, here’s a general response (Disclaimer: This is not clinical advice)..."

    else:
        return "Sorry, I can’t help with that. Please ask an innovation-related question."

    
def export_idea_to_json(fields):
    idea_data = {
        "ideaId": str(uuid.uuid4()),
        "title": fields["title"],
        "abstract": fields["abstract"],
        "problemStatement": fields["problemStatement"],
        "solutionSummary": fields.get("solutionSummary", ""),
        "createdBy": fields["createdBy"],
        "createdOn": datetime.utcnow().isoformat() + "Z",
        "updatedOn": datetime.utcnow().isoformat() + "Z",
        "ideaStatus": "submitted",
        "areaOfImpact": fields["areaOfImpact"],
        "isNewIdea": fields["isNewIdea"],
        "basedOnIdeaId": None,
        "innovationStage": fields["innovationStage"],
        "attachments": [],
        "relatedTechnologies": fields["relatedTechnologies"],
        "impactMetrics": fields["impactMetrics"],
        "reviewComments": [],
        "votes / likes": fields["votes / likes"],
        "feedbackHistory": fields["feedbackHistory"]
    }

    # Save the file
    with open("innovation_idea_output.json", "w") as f:
        json.dump(idea_data, f, indent=4)

    return "Idea exported to innovation_idea_output.json"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        print("Agent:", handle_query(user_input))
