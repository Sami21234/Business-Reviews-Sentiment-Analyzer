import streamlit as st
import pandas as pd

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
    # upload section
    uploaded_file = st.file_uploader(
        label='Uploaded a CSV file of reviews',
        type=['csv']
    )

    if uploaded_file is not None:
        st.success('✅ File uploaded successfully!')
    else:
        st.info('Awaiting file upload...')


with right_col:
    st.subheader("📈 Results")

    # upload section
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)    
        st.write('**Preview of your data:**')
        st.dataframe(df.head(10))
    else:
        st.info("Sentiment results and charts will appear here.")



