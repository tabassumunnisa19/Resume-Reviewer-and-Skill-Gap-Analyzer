# app.py
import streamlit as st
import os
from PIL import Image

from evaluator import evaluate_resume
from utils import extract_text_from_pdf

# ---------------- Page config (MUST be first Streamlit call) ----------------
st.set_page_config(
    page_title="Resume Reviewer",
    layout="wide"
)

# ---------------- Load and resize image ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "image.png")

img = Image.open(IMAGE_PATH)
img = img.resize((500, 400))
st.image(img)

st.title("📄 Resume Reviewer & Skill Gap Analyzer")

# ---------------- App UI ----------------
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

# ---------------- Button Logic ----------------
if st.button("Analyze Resume"):
    if not resume_file or not job_desc:
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_pdf(resume_file)
            result = evaluate_resume(resume_text, job_desc)

        # -------- Handle quota / failure --------
        if result["overall_score"] is None:
            st.error("🚫 Gemini API quota exceeded. Please try again later.")
        else:
            st.success("✅ Analysis Complete")

            st.metric("Overall Score", result["overall_score"])

            st.subheader("📌 Resume Improvements")
            for item in result["resume_improvements"]:
                st.write("- ", item)

            st.subheader("🧠 Final Recommendation")
            st.write(result["final_recommendation"])

            st.subheader("✅ Hiring Decision")
            st.success(result["decision"])
