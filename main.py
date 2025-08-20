from fastapi import FastAPI, UploadFile


app = FastAPI()

@app.post("/file/upload-file")
async def upload_file (file: UploadFile):
    return file
