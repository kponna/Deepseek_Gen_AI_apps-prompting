import openai
import gradio as gr

import os
from dotenv import load_dotenv

load_dotenv() 
api_key = os.getenv("API_KEY")

# Replace with your actual DeepInfra token
API_KEY = api_key

client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepinfra.com/v1/openai",
)

def analyze_sentiment(text):
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": "You are an expert in sentiment analysis."},
                {"role": "user", "content": f"Analyze the sentiment of this text: {text}"}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def sentiment_interface(text):
    return analyze_sentiment(text)

gr.Interface(
    fn=sentiment_interface,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Textbox(label="Sentiment Analysis"),
    title="Sentiment Analysis App"
).launch()
