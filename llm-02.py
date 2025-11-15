import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
  base_url="https://api.groq.com/openai/v1",
  api_key=os.environ.get("GROQ_API_KEY")
)

response = client.responses.create(
  model="llama-3.1-8b-instant",
  instructions="Explique com no maximo 10 palavras",
  input="o que é machine learning?"
)

print(response.output_text)