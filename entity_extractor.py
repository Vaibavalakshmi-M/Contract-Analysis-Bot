import re

def extract_entities(text):

    entities = {
        "Parties": set(),
        "Dates": set(),
        "Money": set(),
        "Locations": set()
    }

    # -------- PARTY EXTRACTION --------
    party_pattern = re.findall(
        r'between\s+(.*?)\s+\(".*?"\)\s+and\s+(.*?)\s+\(".*?"\)',
        text,
        re.IGNORECASE
    )

    for p1, p2 in party_pattern:
        entities["Parties"].add(p1.strip())
        entities["Parties"].add(p2.strip())

    # -------- MONEY EXTRACTION --------
    money_pattern = re.findall(r'INR\s?\d{1,3}(?:,\d{3})+', text)
    for amount in money_pattern:
        entities["Money"].add(amount)

    # -------- DATE EXTRACTION --------
    date_pattern = re.findall(r'\d{1,2}\s\w+\s\d{4}', text)
    for date in date_pattern:
        entities["Dates"].add(date)

    # -------- LOCATION EXTRACTION --------
    if "India" in text:
        entities["Locations"].add("India")

    if "Chennai" in text:
        entities["Locations"].add("Chennai")

    return entities
