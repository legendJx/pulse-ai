from pypdf import PdfReader
import io

def extract_text(file_bytes: bytes) -> list[dict]:
    pdf_stream = io.BytesIO(file_bytes)
    reader = PdfReader(pdf_stream)
    extracted_data = []
    
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        extracted_data.append({
            "page": page_number,
            "content": text
        })

        return extracted_data
    
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50,) -> list[str]:
    if text == 0 or len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size 
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    
    return chunks
