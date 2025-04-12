import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Normalize text by removing special chars and extra spaces"""
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)      # Fix spacing
    return text.lower().strip()

def extract_keywords(text):
    """Improved keyword extraction"""
    doc = nlp(clean_text(text))
    keywords = []
    for token in doc:
        if (not token.is_stop and 
            token.is_alpha and 
            len(token.text) > 2 and
            token.pos_ in ['NOUN', 'PROPN', 'ADJ']):
            keywords.append(token.lemma_)
    return list(set(keywords))  # Remove duplicates

def calculate_similarity(resume, job_desc):
    """Enhanced similarity calculation"""
    try:
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            stop_words='english'
        )
        vectors = vectorizer.fit_transform([clean_text(resume), clean_text(job_desc)])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        return min(100, round(similarity * 110, 2))  # Slightly boosted scoring
    except Exception as e:
        print(f"Similarity error: {str(e)}")
        return 0.0

def calculate_ats_score(resume, job_desc):
    """Complete scoring with better analysis"""
    try:
        score = calculate_similarity(resume, job_desc)
        resume_keywords = extract_keywords(resume)
        job_keywords = extract_keywords(job_desc)
        
        missing = list(set(job_keywords) - set(resume_keywords))
        
        suggestions = []
        if score < 50:
            suggestions.append(f"Add these key terms: {missing[:5]}")
        if 'python' in job_desc.lower() and 'python' not in resume.lower():
            suggestions.append("Highlight Python experience")
            
        return score, {
            'missing_keywords': missing,
            'suggestions': suggestions
        }
    except Exception as e:
        print(f"Scoring error: {str(e)}")
        return 0.0, {'missing_keywords': [], 'suggestions': []}