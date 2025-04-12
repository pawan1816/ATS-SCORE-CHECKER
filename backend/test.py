from app.utils.nlp_processor import calculate_ats_score

# Test data
resume = """
Python developer with 5 years experience. 
Skills: AWS, Flask, machine learning basics.
"""

job_desc = """
Seeking Python developer with:
- Cloud platforms (AWS/Azure)
- Web frameworks (Flask/Django)
- Machine learning basics
"""

score, analysis = calculate_ats_score(resume, job_desc)
print(f"Optimized Score: {score}%")
print("Missing:", analysis['missing_keywords'])