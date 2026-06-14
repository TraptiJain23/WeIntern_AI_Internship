import re
import spacy

nlp=spacy.load("en_core_web_sm")
JOB_TITLES = {
    "travel agent",
    "personal trainer",
    "account manager",
    "software engineer",
    "data analyst",
    "teacher",
    "mechanical engineer",
    "data scientist"
}

def extract_name(text):
    #-------RULE BASED--------
    lines = text.split("\n")

    for line in lines[:15]:

        line = line.strip()

        if not line:
            continue

        # Ignore common headings
        if line.lower() in [
            "resume",
            "curriculum vitae",
            "cv"
        ]:
            continue
            
        if line.lower() in JOB_TITLES:
            continue

        # Usually name is short
        if 2 <= len(line.split()) <= 4:

            if re.match(r'^[A-Za-z\s]+$', line):
                return line.title()
   
    # ---------- SPACY FALLBACK ----------
    doc = nlp(text[:2000])

    for ent in doc.ents:

        if ent.label_ == "PERSON":

            name = ent.text.strip()

            if 2 <= len(name.split()) <= 4:
                return name.title()
    return "Unknown"
