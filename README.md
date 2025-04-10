
# 🤖 AI Resume Classifier & Job Matcher

Build your own AI-powered resume screening tool to analyze resumes, predict suitable job roles, and compare them with job descriptions for better career alignment!

---

## 📌 Overview

**AI Resume Matcher** analyzes resumes and job descriptions to provide insights on job role suitability. It extracts key skills, compares them with job requirements, and calculates a match score to help optimize resumes. The tool also offers improvement suggestions to boost chances of getting hired.


---

## **🧠 How It Works**  


📄 **Upload a Resume (PDF format)**

📝 **Paste the Job Description** into the text area

⌨️ Press Ctrl + Enter to analyze

🔍 The app will:

- **Predict the most suitable Job Role**

- **Show a Match Score between resume and JD**

- **Output a Structured JSON (Skills, Education, Experience, Projects)**

- **Display ❌ Feedback if the resume and JD are not a good match**
---

## **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Venkatesh0610/Resume-Analyzer.git 
cd AI-Resume-Matcher
```

### **2️⃣ Install Required Libraries**  
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

```

### **4️⃣ Run the Application**  
```bash
streamlit run app.py
```


  

---
### **Classification Logic & Score Calculation**  

#### **Skill Extraction**  
- **spaCy** is used for **tokenization** and **NLP processing**. The resume text is processed to identify key skills from predefined skill lists. 
- Skills are checked against both the resume and job description for relevance.
  
#### **Job Role Matching**  
- The algorithm uses the skills extracted from the resume and job description to match the best possible job role. Currently, it predicts a set of **static job roles** based on extracted skills. A more advanced version could use **job role APIs** for dynamic role prediction.

#### **Match Score Calculation**  
- The **match score** is calculated as the ratio of common skills between the resume and job description. The formula used is:  
  \[
  \text{Match Score} = \left( \frac{\text{Number of Common Skills}}{\text{Total Skills in Job Description}} \right) \times 100
  \]
- This score provides a **percentage** indicating how closely the resume aligns with the job description. A higher match score means a better fit for the job.

#### **Improvement Suggestions**  
- If the match score is below a certain threshold (e.g., 70%), the system provides feedback on missing skills from the resume that are present in the job description. This is done by identifying the **unmatched skills** between the two.
---

## **🙋‍♀️ About Me**

I'm Vuggu Anusha, a postgraduate student pursuing MCA with a strong interest in Data Science, Artificial Intelligence, and Natural Language Processing.  
This project reflects my passion for building intelligent tools that solve real-world problems and was developed as part of my learning journey with Social Prachar.
