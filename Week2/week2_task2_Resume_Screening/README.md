# Task 2: Resume Screening AI

## Overview

Resume Screening AI is an NLP-powered application that helps recruiters and hiring teams evaluate resumes 
against a given Job Description (JD). The system automatically extracts information from resumes, 
identifies relevant skills, computes similarity scores, and ranks candidates based on their suitability 
for the role.

The application is built using Python, Streamlit, NLP techniques, and Machine Learning concepts such as TF-
IDF Vectorization and Cosine Similarity.

---
## Live Demo

The application has been deployed using Streamlit Community Cloud.

Access the deployed application here:  [https://resume-screening-ai.streamlit.app](https://resume-screening-ai-project-trapti.streamlit.app/)

---

## Features

- Upload and analyze multiple PDF resumes.
- Extract candidate names, education, and experience details.
- Perform NLP preprocessing using tokenization, stopword removal, and lemmatization.
- Extract skills from resumes and job descriptions.
- Calculate Skill Match Score based on matched skills.
- Compute TF-IDF vectors and Cosine Similarity for resume-job matching.
- Generate a Final Match Score using weighted scoring.
- Rank candidates based on their suitability for the role.
- Generate candidate summary reports.
- Download ranking results in CSV format.
- Interactive and user-friendly Streamlit interface.

---
## Technologies Used

**Frontend/UI:** Streamlit

**Programming Language:** Python

**Libraries & Frameworks:**
- PDFPlumber
- Pandas
- NLTK
- Scikit-learn

**NLP Techniques:**
- Tokenization
- Stopword Removal
- Lemmatization

**Machine Learning Techniques:**
- TF-IDF Vectorization
- Cosine Similarity
---

## Folder Structure

```text
week2_task2_Resume-Screening/
│
├── app.py
├── requirements.txt
├── README.md
├── SampleResumes/
├── Demo/
└── utils/
    ├── pdf_parser.py
    ├── name_extractor.py
    ├── education_extractor.py
    ├── experience_extractor.py
    ├── skill_extractor.py
    ├── preprocessor.py
    └── matcher.py
```

---

## Workflow

1. User uploads one or more PDF resumes.
2. User enters a Job Description.
3. Resume text is extracted using PDFPlumber.
4. NLP preprocessing is performed.
5. Skills are extracted from resumes and the JD.
6. Skill Match Score is calculated.
7. TF-IDF vectors are generated.
8. Cosine Similarity is computed.
9. Final Match Score is generated using weighted scoring.
10. Candidates are ranked based on their scores.
11. Results can be downloaded as a CSV report.

---
## Installation

### Clone the Repository

```bash
git clone https://github.com/traptijain23/Weintern_AI_Internship.git
```

### Navigate to Project Directory

```bash
cd Week2/week2_task2_Resume_Screening
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download NLTK Resources

```bash
python
```

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

Exit Python:

```python
exit()
```

### Run the Application

```bash
streamlit run app.py
```

### Open in Browser

```text
http://localhost:8501
```

---

## Scoring Methodology

### Skill Match Score

Skill Match Score is calculated based on the overlap between skills present in the Job Description and the candidate’s resume.

### Similarity Score

TF-IDF Vectorization and Cosine Similarity are used to measure textual similarity between the resume and the Job Description.

### Final Match Score

```text
Final Match Score =
0.3 × Skill Match Score +
0.7 × Similarity Score
```

Candidates are ranked according to their Final Match Score.

---

## Candidate Summary Report

For each candidate, the application generates:

* Candidate Name
* Top Skills
* Matched Skills
* Skill Match Score
* Similarity Score
* Final Match Score

---

## Future Enhancements

* Advanced skill extraction using Named Entity Recognition (NER)
* Support for DOCX resumes
* AI-based skill inference
* Interactive recruiter dashboard
* Resume recommendations and feedback system

---

## Author

Trapti Jain


