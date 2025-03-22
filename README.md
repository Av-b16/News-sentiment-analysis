---
title: News Sentiment Analysis
emoji: 📊
colorFrom: purple
colorTo: green
sdk: streamlit
sdk_version: "1.43.2"
app_file: app.py
pinned: false
short_description: News sentiment analysis with Hindi audio summary.
---

# News Sentiment Analysis & TTS Application

This application analyzes news articles for sentiment (positive, negative, or neutral) and generates a Hindi Text-to-Speech (TTS) audio report.

---

## Features
- Fetch news articles using `NewsAPI`.
- Perform sentiment analysis using Hugging Face's `transformers`.
- Generate comparative sentiment analysis reports.
- Convert the analysis report to Hindi using `gTTS` (Google Text-to-Speech).
- Interactive Streamlit interface.

---

## Setup Instructions
1. **Clone the repository:**


git clone https://github.com/your-username/news-sentiment-app.git
cd news-sentiment-app


2. Set up a virtual environment (optional but recommended):

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Add your NewsAPI key in api.py: Replace YOUR_NEWSAPI_KEY with your API key:
url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey=YOUR_NEWSAPI_KEY"

5. Run the application:
streamlit run app.py

The application will be available at:
http://localhost:8501
=======


