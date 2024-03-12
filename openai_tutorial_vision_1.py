from dotenv import load_dotenv
import os
from openai import OpenAI
import base64
import requests

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
MODEL="gpt-4-vision-preview"

image_path = "image.jpg"
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {openai_api_key}"
}

payload = {
  "model": MODEL,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "어떤 내용의 이미지인가?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())