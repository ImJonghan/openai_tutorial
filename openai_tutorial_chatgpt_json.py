from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
MODEL="gpt-3.5-turbo"
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model=MODEL,
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)
pass