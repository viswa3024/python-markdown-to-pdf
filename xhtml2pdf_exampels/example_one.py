from fastapi import FastAPI, Response
from xhtml2pdf import pisa
from io import BytesIO

app = FastAPI()


@app.get("/health")
def health():
	return {"status": "up"}

@app.get("/generate-pdf")
def generate_pdf():
    # HTML content for the PDF
    html_content = """
    <html>
    <head>
        <title>PDF Example</title>
    </head>
    <body>
        <h1>Hello, FastAPI and xhtml2pdf!</h1>
        <p>This PDF is generated from HTML content.</p>
    </body>
    </html>
    """

    # Convert HTML to PDF using xhtml2pdf
    pdf_buffer = BytesIO()
    pisa.CreatePDF(html_content, dest=pdf_buffer)
    pdf_buffer.seek(0)

    # Return the PDF as a response
    return Response(content=pdf_buffer.getvalue(), media_type="application/pdf")
