def explain_clause(clause):
    clause_lower = clause.lower()

    if "non-compete" in clause_lower:
        return "Risk: Non-compete clauses may restrict future work opportunities. Suggestion: Reduce duration."

    if "penalty" in clause_lower:
        return "Risk: Financial penalties can be heavy. Suggestion: Negotiate lower penalty."

    if "terminate" in clause_lower:
        return "Risk: Termination without notice can create instability. Suggestion: Add notice period."

    if "confidential" in clause_lower:
        return "Risk: Confidentiality breaches may lead to legal issues. Suggestion: Define scope clearly."

    if "indemnify" in clause_lower:
        return "Risk: Indemnity shifts legal burden. Suggestion: Limit indemnity scope."

    if "unlimited liability" in clause_lower:
        return "Risk: Unlimited liability exposes business to high financial risk. Suggestion: Cap liability."

    if "intellectual property" in clause_lower:
        return "Risk: IP ownership transfer may reduce control. Suggestion: Clarify ownership rights."

    return "This clause defines general responsibilities with low legal risk."
