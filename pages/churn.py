import streamlit as st

st.title("⚠️ Customer Churn Analysis")

st.markdown("""
Analyze the possibility of customer churn based on customer behaviour.
""")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Annual Income",
    min_value=15000,
    max_value=120000,
    value=50000
)

spending = st.slider(
    "Spending Score",
    min_value=1,
    max_value=100,
    value=50
)

if st.button("Analyze Churn Risk"):

    risk_score = 0
    reasons = []

    if spending < 40:
        risk_score += 1
        reasons.append("Low spending activity")

    if income < 40000:
        risk_score += 1
        reasons.append("Low annual income")

    if age > 55:
        risk_score += 1
        reasons.append("Older customer segment")

    if risk_score == 0:

        st.success("🟢 Risk Level: LOW")

        st.write("Reasons:")
        st.write("✓ Good spending behaviour")
        st.write("✓ Healthy customer profile")
        st.write("✓ Strong retention potential")

    elif risk_score == 1:

        st.warning("🟡 Risk Level: MEDIUM")

        st.write("Reasons:")
        for reason in reasons:
            st.write(f"• {reason}")

        st.info(
            "Suggested Action: Send personalized offers and engagement campaigns."
        )

    else:

        st.error("🔴 Risk Level: HIGH")

        st.write("Reasons:")
        for reason in reasons:
            st.write(f"• {reason}")

        st.info(
            "Suggested Action: Immediate retention campaign recommended."
        )

st.markdown("---")

st.subheader("Business Interpretation")

st.markdown("""
- Low Risk → Customer likely to remain active.
- Medium Risk → Customer requires engagement.
- High Risk → Customer may leave without intervention.
""")