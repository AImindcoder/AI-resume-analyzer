import streamlit as st
import PyPDF2
import google.generativeai as genai

# CONFIGURE YOUR GEMINI API KEY HERE
genai.configure(api_key="AIzaSyBtgY5UvIH79eoaevbBCcNDYTdXz5RZgJM")

st.title("SmartCV – AI Resume Mentor (Gemini Powered)")
st.write("Upload your resume and get AI-powered suggestions for improvement.")

# Load Gemini model (use a valid model from the list)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Upload CV
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

if uploaded_file:
    st.success("Resume uploaded successfully!")
    with st.spinner("Analyzing your resume with Gemini..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        prompt = f"""
        You are an AI resume expert. Review this resume and suggest improvements.
        Focus on the following:
        1. Formatting
        2. Technical skills for AI/Computer Science fields
        3. Keywords for scholarships/study abroad in AI
        4. English language tone
        5. Professionalism

        Resume Content:
        {resume_text}
        """

        response = model.generate_content([prompt])  # Pass the prompt as a list
        st.subheader("💡 Suggestions to Improve Your Resume:")
        st.markdown(response.text)
