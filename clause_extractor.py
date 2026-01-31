import re

def extract_clauses(text):
    clauses = re.split(r'\n\d+\.', text)
    cleaned = []

    for clause in clauses:
        clause = clause.strip()
        clause = re.sub(r'[^A-Za-z0-9 ,.-]', ' ', clause)

        if len(clause) > 50:
            cleaned.append(clause)

    return cleaned
