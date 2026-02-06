import re

raw_api_input = """
REPORT_START
User: dev_alex@startup.io | Session: 14:45
Contact: +250 (555) 987-6543
Billing: 4111 2222 3333 4444 (Visa)
Location: https://maps.google.com/office?room=beta
Update: Fixed the <div class='header'> bug. #BugFix2026 #Python
Balance: $4,500.50 | Refund: $120.00
Time Log: 11:30 PM
REPORT_END
"""

def extract_data_from_logs(text_data):
    extracted_report = {
        "emails": [],
        "phones": [],
        "cards": [],
        "urls": [],
        "hashtags": [],
        "money": [],
        "security_flags": []
    }

    # Data Extraction Patterns
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    card_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    hashtag_pattern = r'#\w+'
    price_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

    # Execute extraction
    extracted_report["emails"] = list(set(re.findall(email_pattern, text_data)))
    extracted_report["phones"] = re.findall(phone_pattern, text_data)
    extracted_report["urls"] = re.findall(url_pattern, text_data)
    extracted_report["hashtags"] = re.findall(hashtag_pattern, text_data)
    extracted_report["money"] = re.findall(price_pattern, text_data)

    # Sensitive data handling
    raw_cards = re.findall(card_pattern, text_data)
    for card in raw_cards:
        extracted_report["cards"].append(f"XXXX-XXXX-XXXX-{card[-4:]}")

    # Security validation 
    html_check = re.findall(r'<[^>]+>', text_data)
    if html_check:
        extracted_report["security_flags"].append(f"Blocked {len(html_check)} potential XSS tags.")

    return extracted_report

if __name__ == "__main__":
    final_data = extract_data_from_logs(raw_api_input)
    
    for category, items in final_data.items():
        print(f"{category.upper()}: {items}")
