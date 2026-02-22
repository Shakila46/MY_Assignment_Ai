import streamlit as st
from groq import Groq
from fpdf import FPDF


class AssignmentPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Assignment Report', border=False, ln=1, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')


def create_pdf(name, title, content):
    pdf = AssignmentPDF()
    pdf.add_page()
    
   
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Student Name: {name}", ln=1)
    pdf.cell(0, 10, f"Topic: {title}", ln=1)
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    
   
  
    clean_text = content.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
    clean_text = clean_text.replace('—', '-').replace('–', '-').replace('•', '*')
    
 
    final_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 10, txt=final_text)
    return pdf.output(dest='S').encode('latin-1')


st.set_page_config(page_title="Pro Assignment AI", page_icon="📝")
st.title("🎓 Pro Assignment Humanizer")


client = Groq(api_key=st.secrets["GROQ_API_KEY"])

col1, col2 = st.columns(2)
with col1:
    student_name = st.text_input("Student Name :")
with col2:
    assignment_title = st.text_input("Title:")

user_query = st.text_area("Question:", height=150)


if st.button("Generate Answer"):
    if user_query and student_name and assignment_title:
        with st.spinner('Generating answer...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system", 
                            "content": "You are a human student. Write an academic assignment answer in natural, fluent English. Use paragraphs and avoid using list bullets."
                        },
                        {"role": "user", "content": user_query}
                    ],
                    model="llama-3.3-70b-versatile",
                )
               
                st.session_state.output = chat_completion.choices[0].message.content
                st.success("Successfully generated the answer!")
                st.info(st.session_state.output)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please fill in all the fields before generating the answer.")


if 'output' in st.session_state:
    try:
     
        pdf_bytes = create_pdf(student_name, assignment_title, st.session_state.output)
        
        st.download_button(
            label="📄 Download as PDF",
            data=pdf_bytes,
            file_name=f"{assignment_title}.pdf",
            mime="application/pdf"
        )
    except Exception as pdf_err:
        st.error(f"PDF Error: {pdf_err}")