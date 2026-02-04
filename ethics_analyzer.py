from nltk.sentiment import SentimentIntensityAnalyzer # pyright: ignore[reportMissingImports]
import nltk

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def classify_article(text, keyword_groups):
    categories = set()
    text_lower = text.lower()
    for category, keywords in keyword_groups.items():
        for kw in keywords:
            if kw in text_lower:
                categories.add(category)

    return categories


def severity_score(text, severity_weights):
    score = 0
    text_lower = text.lower()

    for word, weight in severity_weights.items():
        if word in text_lower:
            score += weight

    return score


def analyze_articles(articles, keyword_groups, severity_weights):
    scores = {
        "labor": [],
        "environment": [],
        "animal": []
    }

    evidence = {
        "labor": [],
        "environment": [],
        "animal": []
    }

    for article in articles:
        text = article["text"]
        title = article["title"]
        url = article["url"]

        categories = classify_article(text, keyword_groups)
        severity = severity_score(text, severity_weights)
        sentiment = sia.polarity_scores(text)["compound"]

        combined_score = severity + sentiment * 2

        for category in categories:
            scores[category].append(combined_score)
            evidence[category].append({
                "title": title,
                "url": url,
                "impact": round(combined_score, 2)
            })

    return scores, evidence




def normalize_scores(raw_scores):
    final = {}

    for category, values in raw_scores.items():
        if not values:
            final[category] = 5  # neutral if no data
        else:
            avg = min(values)
            score = max(0, min(10, 5 + avg))
            final[category] = round(score, 1)

    return final
