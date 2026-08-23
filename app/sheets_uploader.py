import json
import os

from app.vaccine_service import VaccineData
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

sample_spreadsheet_id = '1egdK-qVQU4qc_kb3fUD4bEmoYTjJpJ7--9SHL-9d7xE'
user_info = {
    "client_id": os.getenv("SHEETS_CLIENT_ID"),
    "client_secret": os.getenv("SHEETS_CLIENT_SECRET")
}

def upload_to_sheet( data: VaccineData):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Parse file
            auth_data = None
            with open('auth.json', 'r', encoding='utf-8') as file:
                auth_data = json.load(file)
            auth_data.client_id = user_info['client_id']
            auth_data.client_secret = user_info['client_secret']
            creds = Credentials.from_authorized_user_info(auth_data)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    print(creds.to_json())
    return