def classify_contract(text):
    text_lower = text.lower()

    if "employee" in text_lower or "employment" in text_lower:
        return "Employment Agreement"

    elif "lease" in text_lower or "rent" in text_lower:
        return "Lease Agreement"

    elif "vendor" in text_lower or "supply" in text_lower:
        return "Vendor Contract"

    elif "service" in text_lower:
        return "Service Agreement"

    elif "partnership" in text_lower:
        return "Partnership Agreement"

    return "General Contract"
