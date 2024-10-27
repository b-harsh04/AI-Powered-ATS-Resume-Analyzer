from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai
import io


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        ## covert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts=[
            {
                "mime_type":'image/jpeg',
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
## Streamlit app

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)...",type={'pdf'})

if uploaded_file is not None:
    st.write("File Uploaded Succesfuly")

submit1 = st.button("Tell me about the Resume....")

submit2 = st.button("How can i improve my skills?....")
submit3 = st.button("Pecentage Match....")
submit4 = st.button("Visa Sponsorship avalaible or not?....")

input_prompt1 = """
You are an experienced Technical Humar resources manager speciializing in fresh graduate recruitments with tech experience in the field of any one job role of data science, data analysis, big data and AI , 
your  task is to review the provided  Resume against the Job Description for the said profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the required job description
Highlight the strengths and weaknesses of the applicant in relation to the specific job requirements.
"""

input_prompt2 = """
    You are a Technical HR manager specializing in fresher graduate recruitments with expertise in the field of any one job role like Data science, Data Analysis, AI, Big data, 
    your role is to scrutinize the resume in light of the Job description provided. 
    Also, suggest any imporvements that the user can make in order for his resume to be more suited for the job description.
"""
input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one of these job roles of data science, data analyst, Big data and deep ATS functionality.
your task is to evaluate the resume against the provided job description and give the percentage match if the resume matches the provided Job description.
Remember to consider keywords which are relevant to the job role and alsoo relevant in the fields in which you specialize. Done consider vague keywords and common action words as well for the match.
First output should come as a percentage and then the list of keywords which are missing from the resume which are mentioned in the job description.
"""

input_prompt4 = """
You are a skilled Technical HR consultant who is knowledgeable about the visa system in the us like F-1, H1-B, F-1 Opt etc.
Your job is to analyse the job description and check whether the comapny is providing visa sponsorships for international applicants.
First give the output as a sentence whether they are providing the sponsorship or not and in the new line specify what type of sponsorship is the company providing.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content, input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.warning("Please Upload the Resume....")

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2,pdf_content, input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.warning("Please Upload the Resume....")

if submit3:    
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content, input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.warning("Please Upload the Resume....")
    
if submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4,pdf_content, input_text)
        st.subheader("The Response is: ")
        st.write(response)

    else:
        st.warning("Please Upload the Resume....")