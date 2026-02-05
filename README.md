# Food Ethics Analysis Project
This project analyzes food companies input by the user and evaluates their ethical behavior using an automated scoring system built from news coverage. Articles are sourced from The Guardian and processed using natural language techniques to assess how frequently companies are committing ethical or unethical actions.
The goal is to demonstrate how unstructured and overwhelming news data can be transformed into quantitative insights using data engineering, sentiment analysis, and scoring models.

## Live Website
https://food-company-ethics-analyzer.streamlit.app

## Project Overview
Food companies regularly face scrutiny over labor practices and consumer safety. My project created an ethics score for each company through:
- Collecting relevant news articles from The Guardian
- Analyzing article sentiment and keywords
- Aggregating results into a composite ethics score
  
### Key Features
- News Data Collection: Automatic retrieval through The Guardian API
- Ethics Scoring System: Sentiment analysis through VADER
- Normalized Company Scores: Scores are standardized to allow comparison across companies

### Tech Stack
- Python
- Pandas & NumPy
- Natural Language Processing (VADER sentiment analysis)
- News API (The Guardian)
- Streamlit for hosting
- 
### Why This Project Matters
Ethical behavior is increasingly important to consumers. This project demonstrates how public news data can be used to quantify ethical trends and assess corporate responsibility.

### Limitations
- News coverage may not fully represent real-world corporate behavior
- Sentiment analysis can miss nuance or context
- Equal weighting assumes all ethical issues carry the same importance
- Possible irrelevant articles are fetched
- Lack of diverse news sources limits the amount of articles
