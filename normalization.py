# normalization.py

def normalize_result(raw):
    return {
        "overall_score": raw.get("match_score", 0),
        "strengths": raw.get("strengths", []),
        "missing_skills": raw.get("missing_skills", []),
        "resume_improvements": raw.get("improvement_suggestions", []),
        "final_recommendation": raw.get("final_verdict", "")
    }
