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
def generate_marketing_copy(product):
    prompt = f"""
    Write a marketing description for {product}. Include:
    - Target audience (age, interests)
    - Key features
    - Emotional appeal
    - Call-to-action
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": "You are a marketing strategist."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    

gr.Interface(
    fn=generate_marketing_copy,
    inputs=gr.Textbox(label="Product Name", placeholder="E.g., Wireless Noise-Canceling Headphones"),
    outputs=gr.Textbox(label="Marketing Copy"),
    title="Marketing Campaign Assistant",
    allow_flagging="never"
).launch()