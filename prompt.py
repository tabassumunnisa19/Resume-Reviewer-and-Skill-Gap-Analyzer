# prompt.py

def build_prompt(resume_text, job_description):
    return f"""
You are a senior technical recruiter.

Task:
Evaluate the following resume against the given job description.

Evaluation Criteria:
- Skills match
- Relevant experience
- Missing requirements
- Resume clarity and impact

Instructions:
- Be objective and specific
- Do not hallucinate skills
- Base evaluation strictly on the provided content

Output Format (VALID JSON ONLY):
{{
  "match_score": number,
  "strengths": [],
  "missing_skills": [],
  "improvement_suggestions": [],
  "final_verdict": "string"
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""
