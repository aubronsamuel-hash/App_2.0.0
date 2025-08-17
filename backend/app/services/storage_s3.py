import os
from uuid import uuid4
from typing import Optional
from fastapi import UploadFile


async def save_file(file: UploadFile, content: Optional[bytes] = None, directory: str = "uploads") -> str:
    os.makedirs(directory, exist_ok=True)
    data = content if content is not None else await file.read()
    file_id = f"{uuid4().hex}_{file.filename}"
    path = os.path.join(directory, file_id)
    with open(path, "wb") as f:
        f.write(data)
    return path
