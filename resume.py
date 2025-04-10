import streamlit as st
import spacy
import docx
import pdfplumber
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

# Predefined job roles and JD skills
job_roles = ["Data Analyst", "Data Scientist", "AI Specialist", "Data Engineer", "Business Analyst", 
             "Machine Learning Engineer", "Data Engineer", "Quantitative Analyst", "Data Architect", "Research Scientist"]

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

def extract_skills_from_resume(resume_text):
    # Process resume text with spaCy
    doc = nlp(resume_text.lower())
    skills = []
    
    # Sample skills to look for
    skill_keywords = ['sql', 'python', 'excel', 'tableau', 'power bi', 'data visualization', 'vlookup', 'pandas', 'numpy']
    
    # Check for presence of skills
    for token in doc:
        if token.text in skill_keywords:
            skills.append(token.text)
    return set(skills)

def extract_skills_from_jd(jd_text):
    # Process JD text with spaCy
    doc = nlp(jd_text.lower())
    skills = []
    
    # Sample skills to look for in JD
    skill_keywords = ['sql', 'python', 'excel', 'tableau', 'power bi', 'data visualization', 'vlookup', 'pandas', 'numpy']
    
    # Check for presence of skills
    for token in doc:
        if token.text in skill_keywords:
            skills.append(token.text)
    return set(skills)

def get_best_fit_role(resume_skills, jd_skills):
    # Calculate the match score (similarity) between the resume and JD skills
    common_skills = resume_skills.intersection(jd_skills)
    match_score = len(common_skills) / len(jd_skills) * 100  # Percent match score
    
    return common_skills, match_score

# Streamlit UI
st.title("📄 AI Resume Matcher & Job Role Predictor")
st.subheader("Welcome to the AI Resume Matcher & Skill Feedback System")
st.markdown("Match your resume with the job description, get role predictions, and receive feedback to improve your skills.")

# Step 1: Upload Resume
st.markdown("### 🧩 Step 1: Upload Your Resume")
uploaded_file = st.file_uploader("📤 Upload Resume (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    # Step 2: Predict Job Roles Based on Resume
    st.markdown("### 📊 Step 2: Job Role Prediction Based on Resume")
    resume_skills = extract_skills_from_resume(resume_text)
    st.write("### Top Predicted Job Roles:")
    predicted_roles = job_roles  # Dummy roles for now (should be based on resume content analysis)
    for role in predicted_roles:
        st.write(f"- {role}")

    # Step 3: Paste Job Description
    st.markdown("### 📝 Step 3: Paste the Job Description (JD)")
    jd_text = st.text_area("Paste the Job Description here", height=300)
    
    if jd_text:
        # Extract skills from JD
        jd_skills = extract_skills_from_jd(jd_text)

        # Step 4: Match Resume with Job Description
        st.markdown("### 📈 Step 4: Match Prediction")
        common_skills, match_score = get_best_fit_role(resume_skills, jd_skills)
        
        best_fit_role = "Data Analyst"  # Example, should be determined by matching roles in JD and resume
        st.write(f"Best Fit Job Role: {best_fit_role}")
        st.write(f"Match Score: {match_score:.2f}%")

        # Step 5: Skill Feedback
        st.markdown("### 🛠️ Step 5: Feedback")
        st.write("**Skill Feedback:**")
        if match_score < 70:
            missing_skills = jd_skills - resume_skills
            st.write("Based on the JD, you may want to improve or add the following skills:")
            for skill in missing_skills:
                st.write(f"- {skill.capitalize()}")
        else:
            st.write("Great job! Your resume is well-aligned with the job description.")

