import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """Extract keywords from text using spaCy"""
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

def calculate_similarity(resume, job_desc):
    """Calculate similarity score between resume and job description"""
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job_desc])
    return cosine_similarity(vectors[0], vectors[1])[0][0] * 100  # Convert to percentage

def calculate_ats_score(resume, job_desc):
    """Calculate ATS score and provide analysis"""
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