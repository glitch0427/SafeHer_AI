import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_safety_advice(source, destination, travel_time, score):

    prompt = f"""
You are SafeHer AI, an AI assistant focused on women's travel safety.

Journey Details:
- Source: {source}
- Destination: {destination}
- Travel Time: {travel_time}
- Safety Score: {score}/100

Give the response in this format:

🟢 Overall Safety
(2-3 lines)

⚠️ Potential Risks
- Bullet points

✅ Safety Tips
- Bullet points

🚨 Emergency Advice
- Bullet points

Keep the response under 180 words.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text