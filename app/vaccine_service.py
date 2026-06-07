import os
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types
import httpx
from fastapi import UploadFile

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = '''
Collect and return in a JSON format the following information from this document:
- Name of the dog
- Veterinarian or clinic name
- Veterinarian or clinic contact address
- Veterinarian or clinic contact phone number
- Veterinarian or clinic contact email
- Gender
- Vaccine name
- Vaccine date
- Vaccine status
- Vaccine expiration date
- Vaccine dose
- Vaccine manufacturer

Do not attempt to infer any other information from any other source, only include any information that is explicitly stated in the document.
'''

def upload_document(document: UploadFile):
    try:
        data = document.file.read()
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=[
                types.Part(
                    text=prompt
                ),
                types.Part.from_bytes(
                    data=data,
                    mime_type='application/pdf',
                ),
            ],
            config={
                "response_format": {"text": {"mime_type": "application/json"}},
            },
        )
        return response
    except Exception as e:
        print(e)
        return None


        