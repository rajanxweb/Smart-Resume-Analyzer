import pdfplumber
import io

# Dictionary containing skill sets for various IT roles
JOB_SKILLS = {
    "software_engineer": ["python", "java", "c++", "data structures", "algorithms", "git", "sql", "agile", "system design"],
    "backend_developer": ["java", "python", "node.js", "c#", "go", "sql", "nosql", "docker", "rest api", "spring", "linux"],
    "cloud_engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "linux", "terraform", "bash", "ci/cd", "networking"],
    "frontend_developer": ["html", "css", "javascript", "react", "vue", "angular", "typescript", "tailwind", "git", "figma"],
    "data_scientist": ["python", "r", "sql", "pandas", "numpy", "machine learning", "tensorflow", "pytorch", "tableau", "statistics"],
    "cybersecurity": ["linux", "networking", "wireshark", "nmap", "firewalls", "cryptography", "owasp", "incident response", "python"]
}

# Display names for the UI dropdown
JOB_TITLES = {
    "software_engineer": "Software Engineer (General)",
    "backend_developer": "Backend Developer",
    "cloud_engineer": "Cloud / DevOps Engineer",
    "frontend_developer": "Frontend Developer",
    "data_scientist": "Data Scientist",
    "cybersecurity": "Cybersecurity Analyst"
}

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extracts text from a PDF file in memory."""
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + " "
    except Exception as e:
        raise ValueError("Could not read PDF file. It might be corrupted.")
    
    return text.lower()

def analyze_skills(text: str, role_key: str) -> dict:
    """Matches text against specific role skills and calculates score."""
    
    # Fallback to software engineer if key is invalid
    skills_to_check = JOB_SKILLS.get(role_key, JOB_SKILLS["software_engineer"])
    role_name = JOB_TITLES.get(role_key, "Software Engineer")
    
    matched_skills = []
    missing_skills = []

    for skill in skills_to_check:
        if skill in text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills = len(skills_to_check)
    score = round((len(matched_skills) / total_skills) * 100)

    # Dynamic suggestions based on the chosen role
    missing_threshold = total_skills // 2
    if len(missing_skills) > missing_threshold:
        suggestion = f"You need to strengthen your core stack for {role_name} roles."
    elif score > 70:
        suggestion = f"Strong profile! You are well-positioned for {role_name} interviews."
    else:
        suggestion = f"Consider adding more {role_name} focused projects to highlight your skills."

    return {
        "score": score,
        "role_name": role_name,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestion": suggestion
    }