#import libraries
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit.components.v1 as components
import os
import json

#Page Configuration
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="🤖",
    layout="wide"
)

#Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#Gemini Configure
if api_key:
    genai.configure(api_key=api_key)

#Title
st.title("🤖 AI Content Generator")
st.markdown("""
Generate high-quality:

- Blog Posts
- Social Media Captions
- Text Summaries

using Gemini AI.
""")

#Sidebar
with st.sidebar:

    st.header("⚙️ Settings")

    tone = st.selectbox(
        "Tone",
        ["Professional",
         "Casual",
         "Friendly",
         "Persuasive"]
    )

    content_type = st.selectbox(
        "Content Type",
        [
            "Blog Post",
            "Social Media Caption",
            "Text Summary"
        ]
    )

#Gemini Model Function
def generate_content(topic, tone, content_type):

    if content_type == "Blog Post":
        prompt = f"""
        Write a detailed blog post on '{topic}'.

        Tone: {tone}

        Include:
        - Catchy title
        - Introduction
        - Main content with headings
        - Conclusion

        Make it engaging and informative.
        """

    elif content_type == "Social Media Caption":
        prompt = f"""
        Write a social media caption about '{topic}'.

        Tone: {tone}

        Include:
        - Short engaging caption
        - Emojis
        - Relevant hashtags
        """

    else:
        prompt = f"""
        Write a concise summary on '{topic}'.

        Tone: {tone}

        Keep it clear, informative and easy to read.
        """

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text


#Main Input
topic = st.text_area(
    "Enter Topic",
    placeholder="Example: Artificial Intelligence in Education"
)

#Session State
if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""


#Generate Button
generate_btn = st.button("🚀 Generate Content")

if generate_btn:

    if not api_key:
        st.error("API key not found.")

    elif not topic.strip():
        st.warning("Please enter a topic.")

    else:
        try:
            with st.spinner("Generating content..."):

                result = generate_content(
                    topic,
                    tone,
                    content_type
                )

                st.session_state.generated_content = result

        except Exception as e:
            st.error(f"Error: {e}")

#Regenerate Button
regenerate_btn = st.button("🔄 Regenerate")

#Output Section
if st.session_state.generated_content:

    st.subheader("Generated Content")

    st.text_area(
        "Generated Content",
        st.session_state.generated_content,
        height=350
    )

    word_count = len(
        st.session_state.generated_content.split()
    )

    char_count = len(
        st.session_state.generated_content
    )
    # metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Words", word_count)

    with col2:
        st.metric("Characters", char_count)
    # copy button

    copy_text = json.dumps(st.session_state.generated_content)
    
    components.html(
        f"""
        <button
            id="copyBtn"
            onclick="
                navigator.clipboard.writeText({copy_text});
                document.getElementById('copyBtn').innerText='✅ Copied!';
                setTimeout(() => {{
                    document.getElementById('copyBtn').innerText='📋 Copy Content';
                }}, 2000);
            "
            style="
                background-color:#4CAF50;
                color:white;
                padding:10px 20px;
                border:none;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
            📋 Copy Content
        </button>
        """,
        height=70,
    )
  
if regenerate_btn:
    if topic.strip():
        with st.spinner("Regenerating content..."):

            result = generate_content(
                topic,
                tone,
                content_type
            )
            st.session_state.generated_content = result


