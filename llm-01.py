import os
from dotenv import load_dotenv

from groq import Groq

load_dotenv()

client = Groq(
  api_key=os.environ.get("GROQ_API_KEY")
)

response = client.chat.completions.create(
  model="llama-3.1-8b-instant",
  messages=[
    {"role": "system", "content": "Atue como um especialista em machine learning"},
    {"role": "user", "content": "De forma simples, o que é machine learning?"}
  ],
  temperature=0,
  top_p=1
)

print(response.choices[0])