import re

def normalize_hindi(text):
    hindi_to_english = {
        "गोपनीयता": "confidential",
        "जुर्माना": "penalty",
        "समाप्ति": "termination",
        "क्षतिपूर्ति": "indemnity",
        "दायित्व": "liability",
        "प्रतिस्पर्धा निषेध": "non-compete",
        "बौद्धिक संपदा": "intellectual property",
        "भुगतान": "payment",
        "क्षेत्राधिकार": "jurisdiction",
        "स्वचालित नवीनीकरण": "auto-renewal"
    }

    for hindi, english in hindi_to_english.items():
        text = text.replace(hindi, english)

    # Remove remaining Hindi characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text
