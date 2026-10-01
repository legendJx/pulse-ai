from fastapi import FastAPI, File, UploadFile, HTTPException
from ingest import extract_text, chunk_text

app = FastAPI(title="Pulse AI")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Campus Pulse AI API is running!"}

@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    file_bytes = await file.read()
    extracted_pages = extract_text(file_bytes)
    all_chunks = []

    for page in extracted_pages:
        page_chunks = chunk_text(page["content"], chunk_size=500, overlap=50)
        for chunk in page_chunks:
            all_chunks.append({
                "page": page["page"],
                "text": chunk
            })
    
    return {
        "filename": file.filename,
        "totalpages": len(extracted_pages),
        "totalchunks": len(all_chunks),
        "samplechunk": all_chunks[0] if all_chunks else None
    }