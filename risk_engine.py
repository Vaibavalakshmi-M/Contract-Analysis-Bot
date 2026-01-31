def detect_risk(clause):
    clause_lower = clause.lower()

    high_risk_words = [
        "penalty",
        "indemnify",
        "terminate without notice",
        "non-compete",
        "auto-renew",
        "unlimited liability",
        "exclusive ownership"
    ]

    medium_risk_words = [
        "confidential",
        "intellectual property",
        "may terminate",
        "jurisdiction"
    ]

    for word in high_risk_words:
        if word in clause_lower:
            return "High"

    for word in medium_risk_words:
        if word in clause_lower:
            return "Medium"

    return "Low"
