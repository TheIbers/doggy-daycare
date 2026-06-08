import json
import os
import requests
from dotenv import load_dotenv
from fastapi import UploadFile
from google import genai
from google.genai import types
from pydantic import BaseModel
import httpx

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Vaccine(BaseModel):
    name: str
    date: str
    status: str
    expiration_date: str
    dose: str
    manufacturer: str

class VaccineData(BaseModel):
    name: str
    veterinarian: str
    address: str
    phone: str
    email: str
    gender: str
    vaccines: list[Vaccine]

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
            config={"response_mime_type": "application/json", "response_schema": VaccineData},
        )
        return json.loads(response.text)
    except Exception as e:
        print(e)
        return None


        