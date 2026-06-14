import re

def extract_education(text):

    lines = text.split("\n")

    education_keywords = [
        "education",
        "academic background",
        "qualifications"
    ]

    stop_keywords = [
        "experience",
        "employment",
        "work experience",
        "skills",
        "projects",
        "certifications",
        "courses",
        "languages",
        "profile",
        "summary",
        "achievements",
        "accomplishments",
        "hobbies"
    ]

    start_idx = None

    for i, line in enumerate(lines):

        if line.strip().lower() in education_keywords:
            start_idx = i
            break

    if start_idx is None:
        return "Education section not found"

    education_section = []

    for line in lines[start_idx + 1:]:

        clean_line = line.strip().lower()

        if clean_line in stop_keywords:
            break

        education_section.append(line)

    return "\n".join(education_section).strip()