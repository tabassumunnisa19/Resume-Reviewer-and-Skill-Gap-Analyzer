# evaluator.py
import os
import json
import re
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

from prompt import build_prompt
from normalization import normalize_result

# ---------------- Gemini Configuration ----------------
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# ---------------- Hiring Decision ----------------
def hiring_decision(score: int) -> str:
    if score >= 80:
        return "Strong Hire"
    elif score >= 60:
        return "Hire"
    elif score >= 40:
        return "Borderline – Needs Improvement"
    else:
        return "Not a Fit"

# ---------------- Safe JSON Parsing ----------------
def safe_parse_json(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON found in model output")
    return json.loads(match.group())

# ---------------- DEMO RESULT ----------------
def demo_result():
    return {
        "overall_score": 72,
        "resume_improvements": [
            "Quantify achievements with measurable impact",
            "Add cloud deployment or DevOps experience",
            "Highlight leadership or ownership of projects"
        ],
        "final_recommendation": "Good candidate with minor improvements required",
        "decision": "Hire"
    }

# ---------------- Main Evaluator ----------------
def evaluate_resume(resume_text: str, job_description: str, mode: str = "demo") -> dict:
    """
    mode = 'demo' | 'live'
    """

    # ---------- DEMO MODE ----------
    if mode == "demo":
        return demo_result()

    # ---------- LIVE GEMINI MODE ----------
    prompt = build_prompt(resume_text, job_description)

    try:
        response = model.generate_content(prompt)
        raw = safe_parse_json(response.text)
        result = normalize_result(raw)
        result["decision"] = hiring_decision(result["overall_score"])
        return result

    except ResourceExhausted:
        return {
            "overall_score": None,
            "resume_improvements": [],
            "final_recommendation": "Gemini API quota exceeded. Please try again later.",
            "decision": "Unavailable (Quota Exceeded)"
        }

    except Exception as e:
        return {
            "overall_score": None,
            "resume_improvements": [],
            "final_recommendation": f"Processing error: {str(e)}",
            "decision": "Unavailable"
        }
