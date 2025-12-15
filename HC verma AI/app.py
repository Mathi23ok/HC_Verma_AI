import streamlit as st
from rag import ask_physics

st.set_page_config(
    page_title="H.C. Verma AI",
    page_icon="📘",
    layout="centered"
)

st.title("📘 H.C. Verma AI")
st.caption("Concept-based Physics Tutor (Concepts of Physics – Vol 1)")

question = st.text_input(
    "Ask your physics doubt:",
    placeholder="e.g., Why does acceleration remain constant in free fall?"
)

if st.button("Ask HC Verma"):
    if question.strip():
        with st.spinner("Thinking like a physicist..."):
            answer = ask_physics(question)
        st.markdown("### ✅ Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
