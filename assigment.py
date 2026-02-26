import streamlit as st
from groq import Groq
from fpdf import FPDF


if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0


st.set_page_config(page_title="AI Assignment Helper", layout="centered")


st.sidebar.title("📊 Usage Tracker")
st.sidebar.write(f"Number of times used today: **{st.session_state.usage_count}**")
st.sidebar.progress(min(st.session_state.usage_count / 30, 1.0)) # Progress bar එකක්


try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("API Key Not Found. Please set the GROQ_API_KEY in Streamlit secrets.")

st.title("📝 AI Assignment Assistant")
st.write("You can ask any academic question related to Software Quality Assurance, and I'll provide a detailed answer along with a downloadable PDF. You have a limit of 30 free uses per day, so use them wisely!")


question = st.text_area("Question", placeholder="Ex: What is Software Quality Assurance?")

if st.button("Generate Answer"):
    if question:
       
        st.session_state.usage_count += 1
        
        with st.spinner("Generating answer..."):
            try:
                
                
               # AI එකෙන් පිළිතුර ලබාගැනීම (High Temperature + Advanced Prompt)
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system", 
                            "content": """Write a rough, unstructured first draft of an academic response. 
                            DO NOT format it perfectly. DO NOT use introductory or concluding filler sentences (like 'In this essay I will discuss...').
                            Write casually but with academic facts. Make sentences uneven—some extremely short. Some long and winding. 
                            Never use transition words like 'Furthermore', 'Moreover', 'Additionally', or 'In conclusion'. Just jump straight into the next point. 
                            Imagine you are quickly typing your thoughts into a notepad."""
                        },
                        {
                            "role": "user", 
                            "content": f"Answer this directly: {question}"
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.85,  # මේකෙන් අහඹු බව (Randomness) වැඩි කරනවා
                    top_p=0.9,         # මේකෙනුත් වෙනස් වචන තෝරගන්න බල කරනවා
                )
                answer = chat_completion.choices[0].message.content
                st.subheader("Answer:")
                st.write(answer)

               
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, txt=f"Question: {question}\n\nAnswer:\n{answer}")
                
                pdf_output = "assignment_answer.pdf"
                pdf.output(pdf_output)

                with open(pdf_output, "rb") as f:
                    st.download_button("Download as PDF", f, file_name="Assignment_Answer.pdf")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question before generating an answer.")


if st.session_state.usage_count >= 25:
    st.sidebar.warning("You are approaching your daily limit of 30 uses. Please use your remaining attempts wisely!")