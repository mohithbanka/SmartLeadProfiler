import os
import requests
from dotenv import load_dotenv

load_dotenv()
HUNTER_API_KEY = os.getenv('HUNTER_API_KEY')

def get_email(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    response = requests.get(url)
    return response.json()


def score_lead(info):
    score = 0
    email = info.get('email', '')

    if email != 'N/A':
        score += 10
        if not email.startswith(('info@', 'support@', 'contact@')):
            score += 5  # personal or specific email
    if 'linkedin' in info:
        score += 10
    if info.get('title') and info['title'] != 'No title found':
        score += 5

    return score