import requests
import time

def fetch_articles(company, api_key, pages=4, page_size=50):
    url = "https://content.guardianapis.com/search"
    all_articles = []

    for page in range(1, pages + 1):
        params = {
            "q": f'"{company}" AND (company OR corporation OR brand)',
            "page": page,
            "page-size": page_size,
            "section": "environment|world|society",
            "from-date": "2000-01-01",
            "order-by": "relevance",
            "api-key": api_key,
            "show-fields": "bodyText"
        }
        
        response = requests.get(url, params=params)


        data = response.json()
        results = data.get("response", {}).get("results", [])
        all_articles.extend(results)

        time.sleep(0.2) 
    print(f"Total articles fetched: {len(all_articles)}")
    return all_articles
