from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import utils

app = FastAPI(title="Universal IT Resume Scanner")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Pass the dictionary of job roles to populate the dropdown
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "job_roles": utils.JOB_TITLES
    })

@app.post("/scan", response_class=HTMLResponse)
async def scan_resume(
    request: Request, 
    file: UploadFile = File(...),
    role: str = Form(...) # Extracts the selected job from the HTML form
):
    # If errors occur, we must pass job_roles back to keep the dropdown populated
    if not file.filename:
        return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "error": "Please select a file."})

    if not file.filename.lower().endswith('.pdf') or file.content_type != 'application/pdf':
        return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "error": "Only PDF files are supported."})

    try:
        file_bytes = await file.read()
        text = utils.extract_text_from_pdf(file_bytes)

        if not text.strip():
            return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "error": "No readable text found."})

        # Process the text based on the specific role chosen!
        results = utils.analyze_skills(text, role)
        
        return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "results": results})

    except ValueError as ve:
        return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "error": str(ve)})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "job_roles": utils.JOB_TITLES, "error": f"An unexpected error occurred: {str(e)}"})