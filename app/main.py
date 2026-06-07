from fastapi import FastAPI, File, UploadFile
from app.vaccine_service import upload_document
app = FastAPI()

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