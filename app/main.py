from fastapi import FastAPI, File, UploadFile
from app.vaccine_service import upload_document
app = FastAPI()

@app.post("/vaccine")
def get_vaccine_data(document: UploadFile = File(...)):
    # Upload document to Digital Ocean bot, scan and return
    try:
        print(upload_document(document))
    except Exception as e:
        print(e)
        return {"message": "Error uploading document"}

    return {"message": "Vaccine data processed successfully"}