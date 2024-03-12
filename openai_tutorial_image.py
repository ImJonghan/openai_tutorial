from dotenv import load_dotenv
import os
from PIL import Image
import requests
from openai import OpenAI

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
MODEL="dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model=MODEL,
    prompt="멋쟁이 사자가 공부하는 모습을 그려줘",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

# 저장 파일 이름 설정
filename = "image.jpg"
response = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(response.content)
Image.open(filename)