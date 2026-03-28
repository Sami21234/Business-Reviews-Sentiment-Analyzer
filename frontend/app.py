import streamlit as st

st.set_page_config(
    page_title="Business Reviews Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Reviews Sentiment Analyzer")
st.write("Analyze customer reviews and understand sentiment instantly.")

with st.sidebar:
    st.title("⚙️ Controls")
    st.write("Options will appear here as we build.")

st.subheader("📁 Upload Reviews")
st.write("File uploader will go here.")

st.divider()

st.subheader("📈 Results")
st.write("Sentiment results will appear here.")