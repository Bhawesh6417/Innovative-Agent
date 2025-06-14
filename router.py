from memory_handler import chat_history

def route_query(query: str) -> str:
    q = query.lower()

    if any(word in q for word in ["build", "develop", "idea", "proposal", "tool"]):
        return "IDEA"
    elif any(word in q for word in ["status", "find", "search", "record", "update", "innovation id"]):
        return "DB"
    elif "medtech" in q:
        return "MEDTECH"
    return "IRRELEVANT"
