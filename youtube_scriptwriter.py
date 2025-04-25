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

def generate_script(topic):
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": "You are an expert YouTube content creator."},
                {"role": "user", "content": f"Write a detailed YouTube script for a video about '{topic}'."}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
    
def app_interface(topic):
    return generate_script(topic)

gr.Interface(
    fn=app_interface,
    inputs=gr.Textbox(label="Video Topic"),
    outputs=gr.Textbox(label="Generated YouTube Script"),
    title="YouTube Script Writer"
).launch()
