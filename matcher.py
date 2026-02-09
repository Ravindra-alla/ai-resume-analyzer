from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description):
    """
    Calculates the match percentage between resume and job description
    using TF-IDF and Cosine Similarity.
    """
    documents = [resume_text, job_description]
    # Custom token pattern to include +, #, ., and -
    vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r'(?u)\b[\w\.\+\#-]+\b')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate Cosine Similarity
    match_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(match_score * 100, 2)

def get_missing_skills(resume_text, job_description):
    """
    Identifies keywords present in the Job Description that are missing from the Resume.
    This is a basic implementation using set differences of processed words.
    """
    vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r'(?u)\b[\w\.\+\#-]+\b')
    vectorizer.fit([resume_text, job_description])
    feature_names = vectorizer.get_feature_names_out()
    
    resume_tfidf = vectorizer.transform([resume_text]).toarray()[0]
    job_tfidf = vectorizer.transform([job_description]).toarray()[0]
    
    resume_keywords = set([feature_names[i] for i in range(len(feature_names)) if resume_tfidf[i] > 0])
    job_keywords = set([feature_names[i] for i in range(len(feature_names)) if job_tfidf[i] > 0])
    
    missing_skills = list(job_keywords - resume_keywords)
    common_keywords = list(resume_keywords.intersection(job_keywords))
    
    return missing_skills, common_keywords
