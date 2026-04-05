import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# Mock Sentiment Data (will be replaced by real CSV data)
MOCK_SENTIMENT = {
    "Positive": 120,
    "Negative": 45,
    "Neutral": 35    
}

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

# Adding Sentiment Cards
        st.write('**Sentiment Overview:**')
        card1, card2, card3 = st.columns(3)

        with card1:
            st.success('🟢 Positive\n\n### 120 reviews')

        with card2:
            st.error('🔴 Negative\n\n### 45 reviews')

        with card3:
            st.warning('🟡 Neutral\n\n### 35 reviews')

        st.write('---')

# Charts

        st.write('**Sentiment Distribution:**')
        chart_col1, chart_col2 = st.columns(2)

        labels = list(MOCK_SENTIMENT.keys())
        values = list(MOCK_SENTIMENT.values())
        colors = ["#2ecc71", "#e74c3c", "#f39c12"]

        with chart_col1:
            pie_chart = go.Figure(
                data=[go.Pie (
                    labels = labels,
                    values = values,
                    hole = 0.4,
                    marker = dict(colors = colors)
                )]
            )

            pie_chart.update_layout(
                title = 'Sentiment Split',
                showlegend = True,
                height = 350
            )
            st.plotly_chart(pie_chart, use_container_width=True)

        with chart_col2:
            bar_chart = go.Figure(
                    data=[go.Bar(
                    x=labels,
                    y=values,
                    marker=dict(color=colors)
                )]
            )

            bar_chart.update_layout(
                title="Review Counts",
                xaxis_title="Sentiment",
                yaxis_title="Number of Reviews",
                height=350
            )
            st.plotly_chart(bar_chart, use_container_width=True)

# Data Preview
        st.write('---')
        st.write('**Preview of your data:**')
        st.dataframe(df.head(10))
    else:
        st.info("Sentiment results and charts will appear here.")



