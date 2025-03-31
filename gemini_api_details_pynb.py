# -*- coding: utf-8 -*-
"""Gemini_API_Details.pynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wpjQAiy4f2o3bnhn2_076Kk0iUWvvAf2

## SET YOUR API KEY
"""

# Commented out IPython magic to ensure Python compatibility.
# %env GEMINIAPIKEY = "Your_Apı_Key"

"""## CURL REQUEST"""

import requests
import os



headers = {
    'Content-Type': 'application/json',
}

params = {
    'key': os.environ.get("GEMINIAPIKEY"),
}

json_data = {
    'contents': [
        {
            'parts': [
                {
                    'text': 'Explain how AI works',
                },
            ],
        },
    ],
}

response = requests.post(
    'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent',
    params=params,
    headers=headers,
    json=json_data,
)

print(response.json())

"""# GOOGLE SDK İLE ÖRNEK (KÜTÜPHANE KULLANIMI)"""

from google import genai

client = genai.Client(api_key=os.environ.get("GEMINIAPIKEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)

"""## TEXT TO IMAGE EXAMPLE"""

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key = os.environ.get("GEMINIAPIKEY"))

contents = ('Hi, can you create a 3d rendered image of a horse '
            'with wings and a top hat flying over a happy '
            'futuristic scifi city with lots of greenery?')

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

# Bu modeller, 4 tane görsel üretiyor. Biz sadece, ilk görselin çıktısını almak istediğimiz için candidates[0] kullandık.
for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()

"""## IMAGE EDITING WITH GEMINI"""

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

import PIL.Image

image = PIL.Image.open('/content/gemini-native-image.png')

client = genai.Client(api_key=os.environ.get("GEMINIAPIKEY"))

text_input = ('Hi, This is a picture of a fictionary horse.'
            'Can you add a llama next to it? Make it fancy',)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("gemini-edited-image.png")
    image.show()

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

import PIL.Image

image = PIL.Image.open('/content/gemini-edited-image.png')

client = genai.Client(api_key=os.environ.get("GEMINIAPIKEY"))

text_input = ('This is a picture of a horse and llama.'
            'Can you add a  red dragon and donkey from Shrek movie Make this scene a bit interesting.',)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("gemini-edited-image2.png")
    image.show()

"""## WATERMARK CLEANING TEST"""

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

import PIL.Image

image = PIL.Image.open('/content/free-watermark.jpg')

client = genai.Client(api_key=os.environ.get("GEMINIAPIKEY"))

text_input = ('This is a picture of mountain.'
            'Can you please clean up watermarks on mountain?',)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("watermark-cleaned.jpg")
    image.show()