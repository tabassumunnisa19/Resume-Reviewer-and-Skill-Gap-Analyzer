# 🧠 AI Resume Reviewer & Skill Gap Analyzer

An AI-powered Resume Analysis and Suggestion System built using Python and Streamlit.  
This application evaluates resumes against job descriptions, detects skill gaps, calculates match scores, and provides actionable improvement suggestions.

---

## 🚀 Live Demo

🔗 Live Application: [https://resume-reviewer-and-skill-gap-analyzer.streamlit.app](https://resume-reviewer-and-skill-gap-analyzer-5hlugzpvnpjtwtbxz2mvny.streamlit.app/)

💻 GitHub Repository: https://github.com/tabassumunnisa19/Resume-Reviewer-and-Skill-Gap-Analyzer  



---

## 📌 Project Overview

The AI Resume Reviewer is designed to assist job applicants by analyzing resumes and comparing them against job descriptions (JD).

The system extracts relevant skills, evaluates resume relevance, calculates a match score, identifies missing skills, and provides personalized suggestions to improve resume quality.

This project demonstrates:

- NLP-based text preprocessing
- Skill extraction and comparison
- Resume scoring logic
- Modular architecture design
- Interactive UI using Streamlit
- Cloud deployment using Streamlit Community Cloud

---

## ✨ Key Features

- 📄 Upload Resume (PDF format)
- 📝 Input Job Description
- 🧹 Text Cleaning & Normalization
- 🔍 Skill Extraction from Resume & JD
- 📊 Resume Match Score Calculation
- ❌ Missing Skill Identification
- 💡 Smart Resume Improvement Suggestions
- 🎨 Interactive Dashboard with Streamlit
- ☁️ Public Cloud Deployment

---

## 🏗 System Architecture

User Input (Resume + Job Description)  
↓  
Text Extraction (PDF Parsing)  
↓  
Text Cleaning & Normalization  
↓  
Skill Extraction  
↓  
Skill Matching Engine  
↓  
Resume Scoring Logic  
↓  
Suggestion Generation  
↓  
Streamlit Dashboard Output  

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Transformers (if applicable)
- spaCy (if applicable)

---

## 📂 Project Structure

    ai-resume-reviewer/
    │
    ├── app.py                # Streamlit frontend application
    ├── evaluator.py          # Resume scoring & evaluation logic
    ├── normalization.py      # Text preprocessing functions
    ├── prompt.py             # Suggestion generation logic
    ├── utils.py              # Helper utilities
    ├── requirements.txt      # Project dependencies
    └── README.md             # Project documentation

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

git clone https://github.com/tabassumunnisa19/Resume-Reviewer-and-Skill-Gap-Analyzer.git

cd Resume-Reviewer-and-Skill-Gap-Analyzer


### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## ☁️ Deployment Guide (Streamlit Community Cloud)

### Step 1: Push Project to GitHub

git init
git add .
git commit -m "Initial commit - Resume Reviewer and Skill Gap Analyzer"
git branch -M main
git remote add origin https://github.com/tabassumunnisa19/Resume-Reviewer-and-Skill-Gap-Analyzer.git
git push -u origin main

### Step 2: Deploy on Streamlit Cloud

1. Go to: https://share.streamlit.io  
2. Sign in using your GitHub account  
3. Click **New App**
4. Select:
   - Repository: `Resume-Reviewer-and-Skill-Gap-Analyzer`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **Deploy**

After deployment, your app will be live at:

```
https://github.com/tabassumunnisa19/Resume-Reviewer-and-Skill-Gap-Analyzer.streamlit.app
```

Copy that link and update the Live Demo section above.

---

## 📊 How the System Works

1. User uploads a resume in PDF format.
2. Job description is entered manually.
3. The system extracts text from the resume.
4. Text is cleaned and normalized.
5. Skills are extracted from both resume and JD.
6. A matching score is calculated.
7. Missing skills are identified.
8. Improvement suggestions are displayed.

---

## 🎯 Use Cases

- Job seekers improving resumes
- Students preparing for placements
- Recruiters performing initial screening
- Skill gap analysis for career planning

---

## 🔮 Future Enhancements

- Transformer-based semantic similarity scoring
- Advanced Named Entity Recognition (NER)
- Resume formatting feedback
- Multi-role evaluation support
- Batch resume screening
- ATS-style ranking system

---

## 👩‍💻 Author

**Tabassum Unnisa**

If you found this project useful, feel free to ⭐ the repository!








