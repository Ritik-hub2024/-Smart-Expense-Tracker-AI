import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_insights(df):
    summary = df.to_string()

    prompt = f"""
    Analyze the following expense data and give insights:
    {summary}

    Provide:
    - Spending patterns
    - Suggestions to save money
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content