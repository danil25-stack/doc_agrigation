from fastapi import FastAPI, UploadFile, File, Depends
from services.storage.s3_storage_service import S3StorageService, IStorageService
import settings

app = FastAPI()

@app.post("/file/upload-file")
async def upload_file(
    file: UploadFile = File(...),
    storage_service: IStorageService = Depends(S3StorageService),
) -> dict:
    data = await file.read() 
    key = f"article/{file.filename}"
    storage_service.upload_file(
        data, settings.AWS_S3_BUCKET_NAME, key,
    )
    return {"status": "success", "key": key}
  
