# main.py
from scraper import scrape_website
from enrich import get_email
from scorer import score_lead

def run_lead_profiler(domain):
    website_info = scrape_website(f"http://{domain}")
    email_info = get_email(domain)
    email = email_info.get('data', {}).get('emails', [{}])[0].get('value', 'N/A')

    info = {
        "domain": domain,
        "title": website_info.get("title"),
        "email": email
    }
    info['score'] = score_lead(info)
    return info

if __name__ == '__main__':
    domain = input("Enter company domain (e.g., openai.com): ")
    profile = run_lead_profiler(domain)
    print(profile)