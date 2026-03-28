import streamlit as st

st.set_page_config(
    page_title="Business Reviews Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Business Reviews Sentiment Analyzer")
st.write("Upload customer reviews or paste a product URL to analyze sentiment instantly.")
st.divider()

# Sidebar
with st.sidebar:
    st.title("⚙️ Controls")
    st.write('---')
    st.subheader('📁 Data Source')
    st.write("Upload or scrape options will appere here.")
    st.write('---')
    st.subheader('🔧 Settings')
    st.write('Filters and toggles will appear here.')

# Main Layout: Two Columns
left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("📁 Upload Reviews")
    st.info("File uploader will go here.")


with right_col:
    st.subheader("📈 Results")
    st.info("Sentiment results and charts will appear here.")


