from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from app.vaccine_service import upload_document, VaccineData
from app.sheets_uploader import upload_to_sheet

app = FastAPI()
STATIC_DIR = Path(__file__).parent / "static"


@app.get("/", response_class=HTMLResponse)
def index():
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")


@app.post("/vaccine")
def get_vaccine_data(document: UploadFile = File(...)):
    data = None
    # Upload document to Digital Ocean bot, scan and return
    try:
        data = upload_document(document)
    except Exception as e:
        print(e)
        return {"message": "Error uploading document"}

    if data:
        return data
    return {"message": "No response from the agent"}

@app.post("/submit")
def submit_vaccine(data: VaccineData):
    try:
        upload_to_sheet(data)
    except Exception as e:
        print(e)
        return {"message": "Error appending to sheet"}