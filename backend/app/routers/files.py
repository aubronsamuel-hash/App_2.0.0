from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from ..security import require_auth
from ..services.storage_s3 import save_file

router = APIRouter(prefix="/files", tags=["files"], dependencies=[Depends(require_auth)])

MAX_SIZE = 5 * 1024 * 1024


@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    path = await save_file(file, content)
    return {"path": path}
