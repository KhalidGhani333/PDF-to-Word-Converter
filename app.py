import streamlit as st
from pdf2docx import Converter


st.title("📄 PDF to Word Converter")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    output_docx = "Converted.docx"

    # Convert using pdf2docx
    with st.spinner("Converting... Please wait."):
        cv = Converter("uploaded.pdf")
        cv.convert(output_docx, start=0, end=None)
        cv.close()

    # Offer download
    with open(output_docx, "rb") as f:
        st.success("✅ Conversion completed!")
        st.download_button("Download Word File", f, file_name="Converted.docx")


st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size: 12px; color: #888;'>🔧 Built by <strong>Khalid Ghani</strong></p>",
    unsafe_allow_html=True
)