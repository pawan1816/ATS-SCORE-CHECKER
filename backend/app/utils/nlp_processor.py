import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def calculate_ats_score(resume, job_desc):
    # Your existing scoring logic
    score = calculate_similarity(resume, job_desc)
    resume_keywords = set(extract_keywords(resume))
    job_keywords = set(extract_keywords(job_desc))
    
    missing_keywords = list(job_keywords - resume_keywords)
    
    suggestions = []
    if score < 70:
        suggestions.append("Add more keywords from the job description")
    if len(resume.split()) > 800:
        suggestions.append("Reduce resume length to under 800 words")
    
    return score, {
        'missing_keywords': missing_keywords,
        'suggestions': suggestions
    }