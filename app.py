import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Question Answering App",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.main {
    background: transparent;
}
h1, label {
    color: white;
}
.stTextArea textarea, .stTextInput input {
    background-color: #1e293b;
    color: white;
    border-radius: 8px;
}
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1.5em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Question Answering Web App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#cbd5e1;'>Enter text and ask questions</p>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

model = load_model()

context = st.text_area("Context", height=180)
question = st.text_input("Question")

if st.button("Get Answer"):
    if context.strip() and question.strip():
        result = model({"context": context, "question": question})
        st.success(result["answer"])
        st.caption(f"Confidence Score: {round(result['score'], 2)}")
    else:
        st.warning("Please enter both context and question.")

