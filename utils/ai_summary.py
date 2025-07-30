import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_summary(df):
    prompt = f"Summarize key insights from the following dataset:\n\n{df.head(20).to_string()}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating summary: {e}"
