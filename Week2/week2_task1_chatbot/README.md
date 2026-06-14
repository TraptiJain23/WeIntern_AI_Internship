# Task 1 : Career Guidance Chatbot

An AI-powered Career Guidance Chatbot built using Python and Streamlit.

The chatbot helps users explore career paths, required skills, certifications, internships, resumes, interviews, and job search guidance through intent-based conversations.

##  Live Demo

The application is deployed on Streamlit Cloud.

Streamlit App:

https://ai-career-guidance-chatbot-trapti.streamlit.app

## Why Streamlit?

Although the task allowed different implementation options such as Flask, Tkinter, and CLI-based applications, Streamlit was chosen for this project due to my familiarity and comfort with the framework.

Streamlit enabled faster development of the chatbot interface while allowing me to focus more on intent recognition, conversation flow, and context-aware responses rather than frontend development. It also provides a clean and interactive user experience using only Python and supports quick deployment through Streamlit Community Cloud.

This made Streamlit a practical choice for building and demonstrating the Career Guidance Chatbot efficiently.

---

##  Features

- **Intent Recognition using RapidFuzz**  
  Identifies the user's intent by matching queries with predefined patterns using fuzzy string matching.

- **Rule-Based Career Guidance System**  
  Provides career-related guidance through a structured intent-response mechanism.

- **Context-Aware Multi-Turn Conversations**  
  Remembers the user's selected career path and provides relevant follow-up responses for skills and certifications.

- **Career-Specific Recommendations**  
  Offers customized skill requirements and certification suggestions for Data Analyst, Software Developer, Data Scientist, and Cybersecurity roles.

- **Conversation History Logging**  
  Stores user queries and chatbot responses with timestamps in a log file.

- **Interactive Streamlit Chat Interface**  
  Provides a clean and user-friendly web-based chatbot experience.

- **Fallback Handling**  
  Responds gracefully when the user enters an unsupported or unrecognized query.

- **JSON-Based Intent Dataset**  
  Uses a structured JSON file containing patterns and responses for easy maintenance and scalability.

- **Career Development Assistance**  
  Provides guidance related to resumes, interviews, internships, certifications, LinkedIn optimization, projects, and job search.

## Supported Career Domains

- Data Analyst
- Software Developer
- Data Scientist
- Cybersecurity Analyst

## Technologies Used

- Python
- Streamlit
- RapidFuzz
- JSON
- Session state

## Project Structure

```
week2_task1_chatbot/
├── app.py
├── intents.json
├── requirements.txt
├── README.md
├── screenshots/
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
└── demo_video.mp4
```

## Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/TraptiJain23/WeIntern_AI_Internship.git
```

### 2. Navigate to Project Folder

```
cd Week2/week2_task1_chatbot
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Streamlit Application
```
streamlit run app.py
```

The chatbot will open in your browser at:

```text
http://localhost:8501
```

---

## Sample Questions

Try asking:

- hello
- how to become data analyst
- what skills do i need
- which certifications should i do
- how to become software developer
- how to become data scientist
- how to become cybersecurity analyst
- interview tips
- resume tips

## Intent Dataset

The chatbot uses a JSON-based intent dataset containing patterns and responses for career-related queries.

**Supported Intents**

1. greeting
2. goodbye
3. thanks
4. career_options
5. data_analyst
6. software_developer
7. data_scientist
8. cybersecurity
9. skills_required
10. resume_tips
11. interview_preparation
12. internships
13. certifications
14. salary_information
15. linkedin_guidance
16. project_guidance
17. job_search

##  Demo

Screenshots of chatbot conversations are available in the **screenshots/** folder.

A complete walkthrough is provided in **demo_video.mp4**.

## Future Improvements

- Advanced NLP Intent Classification
- LLM Integration (Gemini/OpenAI)
- Personalized Career Recommendations
- Resume Analyzer
- Career Roadmap Generator
- Job Recommendation Engine
- Personalized learning roadmaps

## Author

Trapti Jain
