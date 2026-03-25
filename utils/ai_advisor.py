import os
from dotenv import load_dotenv
from groq import Groq

def get_ai_advice(steps, sleep, heart, stress):
    load_dotenv()  # load env here (important)

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "⚠️ API key not found. Check your .env file."

    client = Groq(api_key=api_key)

    prompt = f"""
    User Health Data:
    Steps: {steps}
    Sleep: {sleep} hours
    Heart Rate: {heart}
    Stress Level: {stress}/10

    Give short, practical health advice in a friendly tone.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content