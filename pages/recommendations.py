import streamlit as st

st.title("📢 Marketing Recommendations")

recommendations = {
    0: "Offer discount coupons and promotional campaigns.",
    1: "Provide loyalty rewards and premium memberships.",
    2: "Use personalized email marketing.",
    3: "Target with seasonal product recommendations.",
    4: "Upsell premium products and exclusive deals."
}

cluster = st.selectbox(
    "Select Customer Cluster",
    [0, 1, 2, 3, 4]
)

st.success(
    recommendations[cluster]
)

st.subheader("General Marketing Tips")

st.markdown("""
- Reward loyal customers.
- Retarget inactive customers.
- Offer personalized promotions.
- Increase engagement using email campaigns.
- Create cluster-specific advertisements.
""")