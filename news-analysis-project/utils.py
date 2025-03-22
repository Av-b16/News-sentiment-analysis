# utils.py
from transformers import pipeline
from gtts import gTTS
import os

# Sentiment Analysis using Hugging Face pipeline
def perform_sentiment_analysis(articles):
    sentiment_model = pipeline("sentiment-analysis")
    results = []
    for article in articles:
        sentiment = sentiment_model(article['summary'])[0]
        results.append({
            'title': article['title'],
            'summary': article['summary'],
            'sentiment': sentiment['label'],
            'score': sentiment['score'],
            'url': article['url']
        })
    return results

# Generate comparative sentiment analysis in English
def generate_comparative_analysis(results):
    positive = sum(1 for result in results if result['sentiment'] == 'POSITIVE')
    negative = sum(1 for result in results if result['sentiment'] == 'NEGATIVE')
    neutral = len(results) - positive - negative
    
    # Report in English
    report = f"Out of {len(results)} articles analyzed:\n"
    report += f"✅ {positive} articles are positive.\n"
    report += f"❌ {negative} articles are negative.\n"
    report += f"⚪ {neutral} articles are neutral."
    return report

# Generate Hindi Text-to-Speech (TTS) using gTTS from the English report
def text_to_speech(text):
    # Convert the English report to Hindi translation for audio
    hindi_translation = translate_to_hindi(text)
    
    try:
        # Generate Hindi audio from translated text
        tts = gTTS(hindi_translation, lang='hi', slow=False)
        
        # Save audio as summary_audio.mp3
        audio_file = "summary_audio.mp3"
        tts.save(audio_file)
        
        print(f"✅ Hindi audio saved as {audio_file}")
        return audio_file
    except Exception as e:
        print(f"❌ Error generating audio: {e}")
        return None

# Simple translation to Hindi (basic mapping for key phrases)
def translate_to_hindi(text):
    # Manual translation of key phrases for the audio
    translation_map = {
        "Out of": "कुल",
        "articles analyzed": "लेखों का विश्लेषण किया गया",
        "articles are positive": "लेख सकारात्मक हैं",
        "articles are negative": "लेख नकारात्मक हैं",
        "articles are neutral": "लेख तटस्थ हैं",
        "positive": "सकारात्मक",
        "negative": "नकारात्मक",
        "neutral": "तटस्थ",
        "✅": "✅",
        "❌": "❌",
        "⚪": "⚪"
    }
    
    # Translate each phrase using translation map
    for eng, hin in translation_map.items():
        text = text.replace(eng, hin)
    
    return text
