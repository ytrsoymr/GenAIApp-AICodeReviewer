import streamlit as st
import google.generativeai as genai
import re

# Set Google API Key (Replace with your actual key securely)
genai.configure(api_key="AIzaSyBtivJRQIbk0EYYXzv12hECw3sEw4K-wB8")

def review_code(code):
    prompt = f"""
    You are an expert Python code reviewer. Review the following Python code, identify any bugs, logical errors, or inefficiencies, 
    and provide suggestions along with a corrected version:

    Code:
    {code}

    Please return the review in the following format:
    - Issues found:
    - Suggested fixes:
    - Corrected Code:
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text  # Extract text from response

def extract_corrected_code(response_text):
    """Extracts corrected Python code from the AI response."""
    match = re.search(r"```python\n(.*?)\n```", response_text, re.DOTALL)
    return match.group(1).strip() if match else "No corrected code found."

# Streamlit UI
st.title("AI Code Reviewer (Google Gemini)")
st.write("Submit your Python code for an AI-powered review!")

code = st.text_area("Paste your Python code here:", height=300)

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Reviewing your code..."):
            review_result = review_code(code)

            # Extract corrected code
            corrected_code = extract_corrected_code(review_result)

            # Display full review feedback (Issues & Fixes)
            st.subheader("Review Feedback:")
            st.text_area("AI Review:", review_result, height=300)

            # Display only the corrected code
            st.subheader("Corrected Code:")
            st.text_area("Fixed Code:", corrected_code, height=300)
    else:
        st.warning("Please enter some Python code.")