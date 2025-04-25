import openai
import gradio as gr
import PyPDF2 
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


def summarize_legal_doc(pdf_file):
    """
    Reads the uploaded PDF using PyPDF2.
    Summarizes the extracted text via DeepSeek-V3 (OpenAI-compatible API).
    Returns the summarized text.
    """
    if pdf_file is None:
        return "No file uploaded."
    
    try: 
        reader = PyPDF2.PdfReader(pdf_file.name)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text() 
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Summarize this legal document into 5 bullet points. "
                        "Highlight obligations, penalties, and termination clauses."
                    )
                },
                {
                    "role": "user",
                    "content": extracted_text
                }
            ],
            temperature=0.2 
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main(): 
    iface = gr.Interface(
        fn=summarize_legal_doc,
        inputs=gr.File(label="Upload PDF Document"),
        outputs=gr.Textbox(label="Summary"),
        title="Legal Document Summarizer"
    ) 
    iface.launch()

if __name__ == "__main__":
    main()