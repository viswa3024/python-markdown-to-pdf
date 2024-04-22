from fastapi import FastAPI
from pdfkit import new

app = FastAPI()


@app.get("/health")
def health():
	return {"status": "up"}

@app.get("/pdf")
def generate_pdf():
	html = "<h1>Hello, World!</h1>"
	return new(html).to_pdf()

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)