# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go

# st.set_page_config(
#     page_title="Business Reviews Sentiment Analyzer",
#     page_icon="📊",
#     layout="wide"
# )

# # Header
# st.title("📊 Business Reviews Sentiment Analyzer")
# st.write("Upload customer reviews or paste a product URL to analyze sentiment instantly.")
# st.divider()

# # Sidebar
# with st.sidebar:
#     st.title("⚙️ Controls")
#     st.write('---')
#     st.subheader('📁 Data Source')
#     st.write("Upload or scrape options will appere here.")
#     st.write('---')
#     st.subheader('🔧 Settings')
#     st.write('Filters and toggles will appear here.')

# # Mock Sentiment Data (will be replaced by real CSV data)
# MOCK_SENTIMENT = {
#     "Positive": 120,
#     "Negative": 45,
#     "Neutral": 35    
# }

# # Main Layout: Two Columns
# left_col, right_col = st.columns([1, 2])

# with left_col:
#     st.subheader("📁 Upload Reviews")

# # upload section
#     uploaded_file = st.file_uploader(
#         label='Uploaded a CSV file of reviews',
#         type=['csv']
#     )

#     if uploaded_file is not None:
#         st.success('✅ File uploaded successfully!')
#     else:
#         st.info('Awaiting file upload...')


# with right_col:
#     st.subheader("📈 Results")

# # upload section
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)    

# # Adding Sentiment Cards
#         st.write('**Sentiment Overview:**')
#         card1, card2, card3 = st.columns(3)

#         with card1:
#             st.success('🟢 Positive\n\n### 120 reviews')

#         with card2:
#             st.error('🔴 Negative\n\n### 45 reviews')

#         with card3:
#             st.warning('🟡 Neutral\n\n### 35 reviews')

#         st.write('---')

# # Charts

#         st.write('**Sentiment Distribution:**')
#         chart_col1, chart_col2 = st.columns(2)

#         labels = list(MOCK_SENTIMENT.keys())
#         values = list(MOCK_SENTIMENT.values())
#         colors = ["#2ecc71", "#e74c3c", "#f39c12"]

#         with chart_col1:
#             pie_chart = go.Figure(
#                 data=[go.Pie (
#                     labels = labels,
#                     values = values,
#                     hole = 0.4,
#                     marker = dict(colors = colors)
#                 )]
#             )

#             pie_chart.update_layout(
#                 title = 'Sentiment Split',
#                 showlegend = True,
#                 height = 350
#             )
#             st.plotly_chart(pie_chart, use_container_width=True)

#         with chart_col2:
#             bar_chart = go.Figure(
#                     data=[go.Bar(
#                     x=labels,
#                     y=values,
#                     marker=dict(color=colors)
#                 )]
#             )

#             bar_chart.update_layout(
#                 title="Review Counts",
#                 xaxis_title="Sentiment",
#                 yaxis_title="Number of Reviews",
#                 height=350
#             )
#             st.plotly_chart(bar_chart, use_container_width=True)

# # Data Preview
#         st.write('---')
#         st.write('**Preview of your data:**')
#         st.dataframe(df.head(10))
#     else:
#         st.info("Sentiment results and charts will appear here.")

# import streamlit as st
# import joblib
# import os

# # Load model and vectorizer
# model = joblib.load("../backend/model/sentiment_model.pkl")
# vectorizer = joblib.load("../backend/model/vectorizer.pkl")

# st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

# st.title("Amazon Review Sentiment Analyzer")
# st.write("Enter a product review and detect whether it is Positive, Neutral, or Negative.")

# review = st.text_area("Enter Review")

# if st.button("Analyze Sentiment"):
#     if review.strip() == "":
#         st.warning("Please enter a review.")
#     else:
#         review_vector = vectorizer.transform([review])
#         prediction = model.predict(review_vector)[0]

#         if prediction == "positive":
#             st.success(f"Sentiment: {prediction} 😊")
#         elif prediction == "neutral":
#             st.info(f"Sentiment: {prediction} 😐")
#         else:
#             st.error(f"Sentiment: {prediction} 😞")


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Business Reviews Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("../backend/model/sentiment_model.pkl")
vectorizer = joblib.load("../backend/model/vectorizer.pkl")

# ---------------- HEADER ----------------
st.title("📊 Business Reviews Sentiment Analyzer")
st.write(
    "Analyze customer reviews either by entering a single review or uploading a CSV file."
)
st.divider()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Controls")
    st.write("---")
    mode = st.radio(
        "Choose Analysis Type",
        ["Single Review", "CSV Upload"]
    )

# ---------------- SINGLE REVIEW MODE ----------------
if mode == "Single Review":
    st.subheader("✍️ Analyze a Single Review")

    review = st.text_area(
        "Enter a customer review:",
        height=150
    )

    if st.button("Analyze Sentiment"):
        if review.strip() == "":
            st.warning("Please enter a review.")
        else:
            review_vector = vectorizer.transform([review])
            prediction = model.predict(review_vector)[0]

            st.write("### Result")

            if prediction == "positive":
                st.success(f"🟢 Positive")
            elif prediction == "neutral":
                st.warning(f"🟡 Neutral")
            else:
                st.error(f"🔴 Negative")

            st.write("**Review:**")
            st.write(review)

# ---------------- CSV MODE ----------------
else:
    st.subheader("📁 Upload Review CSV")

    uploaded_file = st.file_uploader(
        "Upload a CSV file containing reviews",
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### Preview of Uploaded Data")
        st.dataframe(df.head())

        # Find likely review column
        possible_columns = [
            "review",
            "reviews",
            "text",
            "review_text",
            "reviews.text"
        ]

        review_column = None

        for col in possible_columns:
            if col in df.columns:
                review_column = col
                break

        if review_column is None:
            st.error(
                "No review column found. Rename your review column to one of: "
                "`review`, `text`, or `reviews.text`"
            )
        else:
            # Predict sentiments
            review_vectors = vectorizer.transform(df[review_column].astype(str))
            predictions = model.predict(review_vectors)

            df["Predicted Sentiment"] = predictions

            # Count sentiments
            positive_count = (df["Predicted Sentiment"] == "positive").sum()
            neutral_count = (df["Predicted Sentiment"] == "neutral").sum()
            negative_count = (df["Predicted Sentiment"] == "negative").sum()

            # Cards
            st.write("### Sentiment Overview")

            card1, card2, card3 = st.columns(3)

            with card1:
                st.success(f"🟢 Positive\n\n### {positive_count}")

            with card2:
                st.warning(f"🟡 Neutral\n\n### {neutral_count}")

            with card3:
                st.error(f"🔴 Negative\n\n### {negative_count}")

            # Charts
            labels = ["Positive", "Neutral", "Negative"]
            values = [positive_count, neutral_count, negative_count]
            colors = ["#2ecc71", "#f39c12", "#e74c3c"]

            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:
                pie_chart = go.Figure(
                    data=[
                        go.Pie(
                            labels=labels,
                            values=values,
                            hole=0.4,
                            marker=dict(colors=colors)
                        )
                    ]
                )

                pie_chart.update_layout(
                    title="Sentiment Distribution",
                    height=400
                )

                st.plotly_chart(pie_chart, use_container_width=True)

            with chart_col2:
                bar_chart = go.Figure(
                    data=[
                        go.Bar(
                            x=labels,
                            y=values,
                            marker=dict(color=colors)
                        )
                    ]
                )

                bar_chart.update_layout(
                    title="Review Counts",
                    xaxis_title="Sentiment",
                    yaxis_title="Number of Reviews",
                    height=400
                )

                st.plotly_chart(bar_chart, use_container_width=True)

            st.write("### Results Table")
            st.dataframe(df)

            # Download button
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download Results CSV",
                data=csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )
    else:
        st.info("Upload a CSV file to begin analysis.")