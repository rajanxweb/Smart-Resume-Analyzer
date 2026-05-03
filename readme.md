### Step 5: Open it in your browser
Hold `Ctrl` (or `Cmd`) and click the link in your terminal, or manually go to **http://127.0.0.1:8000** in your web browser. Boom! You're ready to scan resumes.

---

## 🧠 How the Logic Works (For Beginners)

Curious about how it scores resumes? It's actually quite simple:
1. In `utils.py`, there is a dictionary (a list of lists) containing the core skills needed for different IT jobs.
2. When you upload a PDF, `pdfplumber` extracts all the text and turns it into lowercase.
3. The app simply searches that text for the keywords associated with your chosen job.
4. If the job requires 10 skills and your resume has 7 of them, your score is 70/100!

---

## 🤝 Contributing

This project is a great starting point, but it can always be better! Feel free to fork thisHere is a complete, beginner-friendly `README.md` for your project. I’ve written it in a conversational, easy-to-follow tone so that anyone—even someone just starting out with coding—can understand what it does and how to run it. 

You can just copy everything inside the code block below and paste it into a file named `README.md` in your project folder!

***
```markdown
# 🚀 Smart Resume Analyzer

Hey there! 👋 Welcome to the **Smart Resume Analyzer**. 

Whether you are a recruiter trying to filter applications or a developer wanting to see if your resume matches a job description, this tool has you covered. It's a lightweight, beautifully designed web application that reads your PDF resume and instantly tells you how well your skills match top IT roles.

🌍 **Live Demo:** [Insert your Render link here once hosted, e.g., https://resume-analyzer-demo.onrender.com]

---

## 🤔 What does it do?

1. **You choose a tech role** (like Backend Developer, Data Scientist, or Cloud Engineer).
2. **You upload your resume** as a PDF.
3. **The app works its magic** by reading the text inside your PDF.
4. **It gives you a score** out of 100, showing exactly which required skills you have and which ones you are missing. 

It also features a sleek, "two-phase" dark-mode interface that physically changes color (Green, Yellow, or Red) based on how good your match score is!

---

## 🛠️ Built With (The Tech Stack)

I kept this project simple, fast, and beginner-friendly. There are no complicated databases or heavy machine learning models. 

* **Backend:** [Python](https://www.python.org/) + [FastAPI](https://fastapi.tiangolo.com/) (For running the server and handling uploads)
* **Frontend:** Standard HTML & CSS (Using Jinja2 for dynamic templates)
* **PDF Parsing:** `pdfplumber` (A handy Python library to read text from PDFs)

---

## 📂 Project Structure

Here is how the project is organized. It's very minimal!

```text
smart-resume-analyzer/
│
├── main.py              # The FastAPI server (the brain of the app)
├── utils.py             # Contains the logic to read PDFs and calculate scores
├── requirements.txt     # List of Python packages needed to run the app
├── .gitignore           # Tells Git to ignore heavy/secret files
│
└── templates/           
    └── index.html       # The beautiful frontend user interface
💻 How to Run it Locally
Want to run this on your own computer? Follow these simple steps!

Step 1: Get the code
First, download or clone this repository to your computer:

Bash
git clone https://github.com/YOUR-USERNAME/smart-resume-analyzer.git
cd smart-resume-analyzer
Step 2: Create a Virtual Environment
A virtual environment keeps this project's files separate from the rest of your computer.

On Windows: python -m venv venv

On Mac/Linux: python3 -m venv venv

Activate it:

On Windows (Git Bash): source venv/Scripts/activate

On Windows (Command Prompt): venv\Scripts\activate

On Mac/Linux: source venv/bin/activate

(You should see (venv) pop up at the start of your terminal line!)

Step 3: Install the Requirements
Tell Python to install the tools we need (like FastAPI and pdfplumber):

Bash
pip install -r requirements.txt
Step 4: Start the Server!
Run the application using Uvicorn (our local web server):

Bash
uvicorn main:app --reload
Step 5: Open it in your browser
Hold Ctrl (or Cmd) and click the link in your terminal, or manually go to http://127.0.0.1:8000 in your web browser. Boom! You're ready to scan resumes.