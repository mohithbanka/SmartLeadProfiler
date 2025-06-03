def score_lead(info):
    score = 0
    email = info.get('email', '')
    linkedin_url = info.get('linkedin_url', '')
    description = info.get('description', '')

    if email and email != 'N/A':
        score += 10
        if not email.startswith(('info@', 'support@', 'contact@')):
            score += 5

    if linkedin_url and linkedin_url != 'N/A':
        score += 10

    if info.get('title') and info['title'] != 'No title found':
        score += 5
    if description and description != 'No description found':
        score += 5

    return score
