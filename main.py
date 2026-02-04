import streamlit as st
from news_fetcher import fetch_articles
from ethics_analyzer import analyze_articles, normalize_scores
from config import NEWS_API_KEY, ETHICS_KEYWORDS, SEVERITY_WEIGHTS

IGNORE_PHRASES = [
    "recipe", "celebrity", "review", "party", "fashion",
    "style", "mourners", "event", "sports"
]

def is_relevant(text, company):
    """
    Returns True if the article mentions the company and does NOT contain ignored phrases.
    """
    text_lower = text.lower()
    if company.lower() not in text_lower:
        return False
    for phrase in IGNORE_PHRASES:
        if phrase in text_lower:
            return False
    return True


def overall_rating(scores):
    for score in scores.values():
        if score < 3:
            return "❌ Unethical"
    avg = sum(scores.values()) / len(scores)
    if avg >= 5:
        return "✅ Ethical. No controversial or relevant articles found. "
    elif avg >= 3:
        return "⚠️ Mixed"
    else:
        return "❌ Unethical"


st.set_page_config(page_title="Food Ethics Analyzer", layout="wide")

st.title("Food Company Ethics Analyzer")
st.write("Analyze food companies using real Guardian reporting.")

company = st.text_input("Enter a food company name")

if st.button("Analyze") and company:
    with st.spinner("Fetching articles and analyzing ethics..."):
        raw_articles = fetch_articles(company, NEWS_API_KEY)

        # Filter out irrelevant articles
        articles = []
        for article in raw_articles:
            text = article.get("fields", {}).get("bodyText") or article.get("webTitle", "")
            if is_relevant(text, company):
                articles.append(article)

        st.info(f"Total relevant articles after filtering: {len(articles)}")

        if not articles:
            st.error("No articles found.")
        else:
            structured_articles = []
            for article in articles:
                text = article.get("fields", {}).get("bodyText")
                if not text:
                    text = article.get("webTitle")

                structured_articles.append({
                    "text": text,
                    "title": article.get("webTitle"),
                    "url": article.get("webUrl")
                })

            raw_scores, evidence = analyze_articles(
                structured_articles,
                ETHICS_KEYWORDS,
                SEVERITY_WEIGHTS
            )

            scores = normalize_scores(raw_scores)

            st.subheader("Ethics Scores")
            for category, score in scores.items():
                st.metric(category.capitalize(), f"{score}/10")

            st.subheader("Overall Assessment")
            st.write(overall_rating(scores))
            st.caption(f"{len(structured_articles)} articles analyzed")

            st.subheader("Most Impactful Articles")
            for category, items in evidence.items():
                if not items:
                    continue

                st.markdown(f"### {category.capitalize()}")
                worst = sorted(items, key=lambda x: x["impact"])[:3]

                for art in worst:
                    st.write(f"**{art['title']}**")
                    st.write(f"Impact score: {art['impact']}")
                    st.write(art["url"])
