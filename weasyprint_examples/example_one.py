from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import weasyprint
import os

app = FastAPI()

# Create a simple HTML template
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample PDF</title>
    <style>
        h1 {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>Welcome to FastAPI PDF Generation!</h1>
    <p>This is a simple example of generating a PDF from HTML content.</p>
</body>
</html>
"""


@app.get("/health")
def health():
	return {"status": "up"}

@app.get("/generate-pdf")
def generate_pdf():
    # Create a temporary PDF file
    pdf_file_path = "sample.pdf"

    # Convert HTML content to PDF
    weasyprint.HTML(string=html_content).write_pdf(pdf_file_path)

    if not os.path.exists(pdf_file_path):
        raise HTTPException(status_code=500, detail="Failed to generate PDF")

    # Return the PDF file as a response
    return FileResponse(pdf_file_path, filename="sample.pdf", media_type="application/pdf")

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)