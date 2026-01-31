def classify_clause_type(clause):
    clause_lower = clause.lower()

    if "shall not" in clause_lower or "must not" in clause_lower:
        return "Prohibition"

    elif "shall" in clause_lower or "must" in clause_lower:
        return "Obligation"

    elif "may" in clause_lower:
        return "Right"

    else:
        return "General"
