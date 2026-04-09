
# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import joblib

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Business Reviews Sentiment Analyzer",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------- LOAD MODEL ----------------
# model = joblib.load("../backend/model/sentiment_model.pkl")
# vectorizer = joblib.load("../backend/model/vectorizer.pkl")

# # ---------------- HEADER ----------------
# st.title("📊 Business Reviews Sentiment Analyzer")
# st.write(
#     "Analyze customer reviews either by entering a single review or uploading a CSV file."
# )
# st.divider()

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.header("⚙️ Controls")
#     st.write("---")
#     mode = st.radio(
#         "Choose Analysis Type",
#         ["Single Review", "CSV Upload"]
#     )

# # ---------------- SINGLE REVIEW MODE ----------------
# if mode == "Single Review":
#     st.subheader("✍️ Analyze a Single Review")

#     review = st.text_area(
#         "Enter a customer review:",
#         height=150
#     )

#     if st.button("Analyze Sentiment"):
#         if review.strip() == "":
#             st.warning("Please enter a review.")
#         else:
#             review_vector = vectorizer.transform([review])
#             prediction = model.predict(review_vector)[0]

#             st.write("### Result")

#             if prediction == "positive":
#                 st.success(f"🟢 Positive")
#             elif prediction == "neutral":
#                 st.warning(f"🟡 Neutral")
#             else:
#                 st.error(f"🔴 Negative")

#             st.write("**Review:**")
#             st.write(review)
#             def highlight_sentiment(val):
#                 if val == "negative":
#                     return "background-color: #ffcccc"  # light red
#                 elif val == "neutral":
#                     return "background-color: #fff3cd"  # light yellow
#                 else:
#                     return "background-color: #d4edda"  # light green

#             styled_df = df.style.applymap(highlight_sentiment, subset=["Predicted Sentiment"])
#             st.dataframe(styled_df)

# # ---------------- CSV MODE ----------------
# else:
#     st.subheader("📁 Upload Review CSV")

#     uploaded_file = st.file_uploader(
#         "Upload a CSV file containing reviews",
#         type=["csv"]
#     )

#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)

#         st.write("### Preview of Uploaded Data")
#         st.dataframe(df.head())

#         # Find likely review column
#         possible_columns = [
#             "review",
#             "reviews",
#             "text",
#             "review_text",
#             "reviews.text"
#         ]

#         review_column = None

#         for col in possible_columns:
#             if col in df.columns:
#                 review_column = col
#                 break

#         if review_column is None:
#             st.error(
#                 "No review column found. Rename your review column to one of: "
#                 "`review`, `text`, or `reviews.text`"
#             )
#         else:
#             # Predict sentiments
#             review_vectors = vectorizer.transform(df[review_column].astype(str))
#             predictions = model.predict(review_vectors)

#             df["Predicted Sentiment"] = predictions

#             # Count sentiments
#             positive_count = (df["Predicted Sentiment"] == "positive").sum()
#             neutral_count = (df["Predicted Sentiment"] == "neutral").sum()
#             negative_count = (df["Predicted Sentiment"] == "negative").sum()

#             # Cards
#             st.write("### Sentiment Overview")

#             card1, card2, card3 = st.columns(3)

#             with card1:
#                 st.success(f"🟢 Positive\n\n### {positive_count}")

#             with card2:
#                 st.warning(f"🟡 Neutral\n\n### {neutral_count}")

#             with card3:
#                 st.error(f"🔴 Negative\n\n### {negative_count}")

#             # Charts
#             labels = ["Positive", "Neutral", "Negative"]
#             values = [positive_count, neutral_count, negative_count]
#             colors = ["#2ecc71", "#f39c12", "#e74c3c"]

#             chart_col1, chart_col2 = st.columns(2)

#             with chart_col1:
#                 pie_chart = go.Figure(
#                     data=[
#                         go.Pie(
#                             labels=labels,
#                             values=values,
#                             hole=0.4,
#                             marker=dict(colors=colors)
#                         )
#                     ]
#                 )

#                 pie_chart.update_layout(
#                     title="Sentiment Distribution",
#                     height=400
#                 )

#                 st.plotly_chart(pie_chart, use_container_width=True)

#             with chart_col2:
#                 bar_chart = go.Figure(
#                     data=[
#                         go.Bar(
#                             x=labels,
#                             y=values,
#                             marker=dict(color=colors)
#                         )
#                     ]
#                 )

#                 bar_chart.update_layout(
#                     title="Review Counts",
#                     xaxis_title="Sentiment",
#                     yaxis_title="Number of Reviews",
#                     height=400
#                 )

#                 st.plotly_chart(bar_chart, use_container_width=True)

#                 filter = st.multiselect(
#                 "Filter by Sentiment",
#                 ["positive", "neutral", "negative"],
#                 default=["positive", "neutral", "negative"]
#             )

#                 filtered_df = df[df["Predicted Sentiment"].isin(filter)]

#             st.write("### Results Table")
#             st.dataframe(df)

#             # Download button
#             csv = df.to_csv(index=False).encode("utf-8")

#             st.download_button(
#                 label="⬇️ Download Results CSV",
#                 data=csv,
#                 file_name="sentiment_results.csv",
#                 mime="text/csv"
#             )
#     else:
#         st.info("Upload a CSV file to begin analysis.")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import joblib
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.email_utils import send_email




# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Business Reviews Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("../backend/model/sentiment_model.pkl")
vectorizer = joblib.load("../backend/model/vectorizer.pkl")

# ---------------- RESPONSE TEMPLATES ----------------        # <-- NEW (Place 1)
response_templates = {
    "positive": "Thank you so much for your kind words! 😊 We're thrilled you had a great experience with us.",
    "neutral":  "Thank you for your feedback! We're always working to improve your experience.",
    "negative": "We're sorry to hear about your experience. 😔 We'd love to make it right - please contact our support team."
}

# ---------------- HIGHLIGHT FUNCTION ----------------        # <-- NEW (Place 1)
def highlight_sentiment(val):
    if val == "negative":
        return "background-color: #ffcccc; color: black"
    elif val == "neutral":
        return "background-color: #fff3cd; color: black"
    else:
        return "background-color: #d4edda; color: black"

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
                st.success("🟢 Positive")
            elif prediction == "neutral":
                st.warning("🟡 Neutral")
            else:
                st.error("🔴 Negative")

            st.write("**Review:**")
            st.write(review)

            # ---------------- RESPONSE SUGGESTION ----------------    # <-- NEW (Place 2)
            st.write("### 💬 Suggested Response")
            st.info(response_templates[prediction])

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

            # Add suggested responses column
            df["Suggested Response"] = df["Predicted Sentiment"].map(response_templates)

            # Count sentiments
            positive_count = (df["Predicted Sentiment"] == "positive").sum()
            neutral_count  = (df["Predicted Sentiment"] == "neutral").sum()
            negative_count = (df["Predicted Sentiment"] == "negative").sum()

            # ---------------- CARDS ----------------
            st.write("### Sentiment Overview")

            card1, card2, card3 = st.columns(3)

            with card1:
                st.success(f"🟢 Positive\n\n### {positive_count}")
            with card2:
                st.warning(f"🟡 Neutral\n\n### {neutral_count}")
            with card3:
                st.error(f"🔴 Negative\n\n### {negative_count}")

            # ---------------- CHARTS ----------------
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
                pie_chart.update_layout(title="Sentiment Distribution", height=400)
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

    # # ---------------- REPORT GENERATION ----------------
    # st.write("### 📄 Generate Report")
    # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # from backend.llm_summary import generate_llm_summary
    # from backend.email_utils import send_email
    # from backend.pdf_utils import create_pdf
    
    # email = st.text_input("Enter email to send report")

    # if st.button("📧 Generate & Send Report"):

    #     # ✅ STEP 1: CREATE REPORT FIRST
    #     report = generate_report(df)

    #     # ✅ STEP 2: Prepare reviews for LLM
    #     neg_reviews = df[df["Predicted Sentiment"] == "negative"][review_column].head(10)
    #     pos_reviews = df[df["Predicted Sentiment"] == "positive"][review_column].head(5)

    #     sample_reviews = pd.concat([neg_reviews, pos_reviews])
    #     all_reviews_text = " ".join(sample_reviews.astype(str).tolist())

    #     # ✅ STEP 3: LLM summary
    #     with st.spinner("🤖 Generating AI insights..."):
    #         llm_summary = generate_llm_summary(all_reviews_text)

    #     report += f"\n\n🤖 AI Insights:\n{llm_summary}"

    #     # ✅ STEP 4: SHOW REPORT
    #     st.success("Report Generated!")
    #     st.text_area("Preview Report", report, height=300)

    #     # ✅ STEP 5: CREATE PDF
    #     pdf_file = create_pdf(report)

    #     # ✅ STEP 6: DOWNLOAD BUTTON
    #     with open(pdf_file, "rb") as f:
    #         st.download_button(
    #             "📎 Download PDF Report",
    #             f,
    #             file_name="report.pdf"
    #         )

    #     # ✅ STEP 7: SEND EMAIL
    #     if email:
    #         send_email(report, email, pdf_file)
    #         st.success("✅ Email sent successfully!")
    #     else:
    #         st.warning("Please enter an email address")

            # ---------------- REPORT GENERATION ----------------
        st.write("### 📄 Generate Report")

        def generate_report(df):
            total = len(df)
            pos = (df["Predicted Sentiment"] == "positive").sum()
            neu = (df["Predicted Sentiment"] == "neutral").sum()
            neg = (df["Predicted Sentiment"] == "negative").sum()

            # Top negative reviews
            top_neg = df[df["Predicted Sentiment"] == "negative"] \
                        .head(5)[review_column].tolist()

            report = f"""
        📊 Business Review Summary

        Total Reviews: {total}

        🟢 Positive: {pos} ({(pos/total)*100:.1f}%)
        🟡 Neutral: {neu} ({(neu/total)*100:.1f}%)
        🔴 Negative: {neg} ({(neg/total)*100:.1f}%)

        ⚠️ Top Negative Reviews:
        """

            for i, review in enumerate(top_neg, 1):
                report += f"\n{i}. {review}"

            return report


        # Button
        email = st.text_input("Enter email to send report")

        if st.button("📧 Generate & Send Report"):
            report = generate_report(df)

            st.success("Report Generated!")
            st.text_area("Preview Report", report, height=300)

            if email:
                send_email(report, email)
                st.success("✅ Email sent successfully!")
            else:
                st.warning("Please enter an email address")
            # ---------------- FILTER TOGGLES ----------------        # <-- NEW (Place 3)
            st.write("### 🔍 Filter Reviews")

            selected_sentiments = st.multiselect(
                "Show reviews with sentiment:",
                options=["positive", "neutral", "negative"],
                default=["positive", "neutral", "negative"]
            )

            filtered_df = df[df["Predicted Sentiment"].isin(selected_sentiments)]

            st.write(f"Showing **{len(filtered_df)}** of **{len(df)}** reviews")

                 

            # ---------------- HIGHLIGHTED TABLE ----------------        # <-- NEW (Place 4)
            st.write("### Results Table")

            styled_df = filtered_df.style.applymap(
                highlight_sentiment,
                subset=["Predicted Sentiment"]
            )

            st.dataframe(styled_df, use_container_width=True)

            # ---------------- DOWNLOAD BUTTON ----------------
            csv = filtered_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download Results CSV",
                data=csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )

    else:
        st.info("Upload a CSV file to begin analysis.")