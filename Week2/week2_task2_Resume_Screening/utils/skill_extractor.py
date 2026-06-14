SKILLS = [
    "python",
    "sql",
    "java",
    "c++",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "streamlit",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github",
    "figma",
    "canva",
    "adobe photoshop",
    "adobe illustrator",
    "mongodb",
    "react.js",
    "node.js",
    "express.js",
    "mern stack"  
]

def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
