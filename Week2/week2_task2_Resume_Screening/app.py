import streamlit as st
import pandas as pd
from utils.pdf_parser import extract_text_from_pdf
from utils.name_extractor import extract_name
from utils.education_extractor import extract_education
from utils.experience_extractor import extract_experience
from utils.preprocessor import preprocess_text
from utils.skill_extractor import extract_skills
from utils.matcher import (
    calculate_skill_match,
    calculate_similarity
)


st.title("Resume Screening AI")
uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)


st.subheader("Job Description")
job_description = st.text_area(
    "Paste Job Description Here",
    height=200,
    placeholder="Enter job description..."
)


if uploaded_files and job_description:
    results = []

    for idx, file in enumerate(uploaded_files):

        text = extract_text_from_pdf(file)

        st.subheader(f"📄 {file.name}")

        #Extracting Candidate Name

        name = extract_name(text)
        st.write("### Candidate Name")
        st.success(name)

        

        processed_text = preprocess_text(text)
        jd_processed = preprocess_text(job_description)

        resume_skills = extract_skills(processed_text)
        jd_skills = extract_skills(jd_processed)

        st.write("### Resume Skills")
        st.success(", ".join(resume_skills) if resume_skills else "No skills found")

        st.write("### JD Skills")
        st.info(", ".join(jd_skills) if jd_skills else "No skills found")
        

        skill_score, matched_skills = calculate_skill_match(
            jd_skills,
            resume_skills
        )

        st.write("### Matched Skills")
        st.success(
            ", ".join(matched_skills)
            if matched_skills
            else "No matching skills"
        )

        st.write("### Skill Match Score")
        st.info(f"{skill_score}%")

        similarity_score = calculate_similarity(
            jd_processed,
            processed_text
        )

        st.write("### Similarity Score")
        st.info(f"{similarity_score}%")

        final_score = round(
            (0.3 * skill_score) +
            (0.7 * similarity_score),
            2
        )
        #Final Score
        st.write("### Final Match Score")
        st.success(f"{final_score}%")

        results.append({
            "Resume": file.name,
            "Name": name,
            "Match Score": final_score,
            "Skill Score": skill_score,
            "Similarity Score": similarity_score
        })


        st.text_area(
            f"Content of {file.name}",
            value=text,
            height=250,
            key=f"resume_{idx}"
        )

        #Extracting Education section

        education = extract_education(text)
        st.write("### Education")
        st.info(education)

        #Extracting Experience section

        experience = extract_experience(text)
        st.write("### Experience")
        st.info(experience)


        st.subheader("📋 Candidate Summary")

        st.write(f"Name: {name}")

        st.write(
            f"Top Skills: {', '.join(resume_skills[:5])}"
        )

        st.write(
            f"Matched Skills: {', '.join(matched_skills)}"
        )
        
        st.write(
            f"Match Score: {final_score}%"
        )

        

    if results:

        ranking_df = pd.DataFrame(results)

        ranking_df = ranking_df.sort_values(
            by="Match Score",
            ascending=False
        )

        ranking_df.index = range(
            1,
            len(ranking_df) + 1
        )

        st.subheader("🏆 Candidate Rankings")

        st.dataframe(ranking_df)
        csv = ranking_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "📥 Download Ranking Report",
            data=csv,
            file_name="candidate_ranking.csv",
            mime="text/csv"
        )

    st.write("Files uploaded:", len(uploaded_files))

