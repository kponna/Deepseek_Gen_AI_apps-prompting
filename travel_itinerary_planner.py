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

def plan_itinerary(destination, days, interests):
    prompt = f"""
    Create a {days}-day itinerary for {destination}. Focus on {interests}.
    Include:
    - Morning/Afternoon/Evening activities
    - Local cuisine recommendations
    - Transportation tips
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": "You are a travel expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
gr.Interface(
    fn=plan_itinerary,
    inputs=[
        gr.Textbox(label="Destination"),
        gr.Number(label="Number of Days"),
        gr.Dropdown(["Adventure", "Cultural", "Relaxation"], label="Interests")
    ],
    outputs=gr.Textbox(label="Itinerary"),
    title="Travel Itinerary Planner"
).launch()