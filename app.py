import streamlit as st

st.set_page_config(
    page_title="AI Customer Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Driven Customer Analytics Platform")

st.markdown("---")

st.markdown("""
### Transform Customer Data into Business Insights

This platform helps businesses:

- Identify valuable customers
- Segment customer groups using Machine Learning
- Predict purchasing behavior
- Predict customer churn
- Generate business reports
- Improve marketing strategies
""")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Modules",
        "5"
    )

with c2:
    st.metric(
        "ML Algorithms",
        "3"
    )

with c3:
    st.metric(
        "Reports",
        "PDF + Excel"
    )

st.markdown("---")

st.info("""
Use the navigation menu on the left to access:

📊 Dashboard

🛒 Purchase Prediction

⚠️ Churn Prediction

📢 Recommendations

📄 Report Generator
""")

st.markdown("---")

st.caption(
    "Built using Python, Scikit-Learn, Plotly and Streamlit"
)