import os
from fastapi import APIRouter, File, Form, UploadFile
from typing import Optional

router = APIRouter()

UPLOAD_FOLDER = "uploads"

# Pastikan folder uploads ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.get("/test")
def test():
    data = aduuh()
    return data

@router.get("/test")
def test_endpoint():
    return{"message":"endpoint test active"}


def aduuh ():
    return {
        "message" : "dari form 2"
    }

@router.post("/upload-image")
def upload_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@router.post("/upload-single")
def upload_single_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": file_location
    }

@router.post("/upload-multiple")
def upload_multiple_files(files: list[UploadFile] = File(...)):
    saved_files = []
    for file in files:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        saved_files.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "saved_to": file_location
        })
    return saved_files

@router.post("/upload-data")
def upload_data(
    nama_kegiatan: str = Form(...),  # Data JSON dikirim sebagai form field
    files: list[UploadFile] = File(...)  # File dikirim sebagai array atau single
):
    saved_files = []
    for file in files:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        saved_files.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "saved_to": file_location
        })
    return {
        "nama_kegiatan": nama_kegiatan,
        "uploaded_files": saved_files
    }