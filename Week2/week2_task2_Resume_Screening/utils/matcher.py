from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_skill_match(jd_skills, resume_skills):

    if not jd_skills:
        return 0, []

    matched_skills = list(
        set(jd_skills).intersection(set(resume_skills))
    )

    score = (
        len(matched_skills) / len(jd_skills)
    ) * 100

    return round(score, 2), matched_skills

#TF-IDF + Cosine Similarity   
def calculate_similarity(job_description, resume_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [job_description, resume_text]
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(similarity * 100, 2)