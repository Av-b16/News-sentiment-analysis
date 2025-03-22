# app.py
import streamlit as st
from api import fetch_news_api
from utils import perform_sentiment_analysis, generate_comparative_analysis, text_to_speech

# Main Streamlit UI
st.title("📰 News Sentiment Analysis & Hindi TTS")
st.write("Analyze news articles and generate a sentiment-based report with Hindi audio.")

# User input
company_name = st.text_input("🔍 Enter the company name for news analysis:")

# Button to trigger analysis
if st.button("Analyze"):
    if company_name:
        # Fetch news articles
        articles = fetch_news_api(company_name)
        
        if articles:
            # Perform sentiment analysis
            sentiments = perform_sentiment_analysis(articles)
            
            # Generate comparative analysis in English
            analysis_report = generate_comparative_analysis(sentiments)
            
            # Generate Hindi Text-to-Speech (TTS) from the English report
            audio_file = text_to_speech(analysis_report)
            
            # Display results
            st.subheader("📊 Sentiment Analysis Summary")
            st.write(analysis_report)  # Display English text report
            
            # Display articles with sentiments
            for article in sentiments:
                st.markdown(f"**{article['title']}**")
                st.write(f"📝 Summary: {article['summary']}")
                st.write(f"📈 Sentiment: {article['sentiment']} (Confidence: {article['score']:.2f})")
                st.markdown(f"[Read Full Article]({article['url']})")
                st.write("---")
            
            # Play the generated Hindi audio
            if audio_file:
                st.subheader("🎧 Listen to the Hindi Audio Summary")
                st.audio(audio_file, format="audio/mp3")
            else:
                st.error("❌ Error generating audio.")
        else:
            st.warning("⚠️ No articles found. Try another company or keyword.")
    else:
        st.warning("⚠️ Please enter a valid company name.")
