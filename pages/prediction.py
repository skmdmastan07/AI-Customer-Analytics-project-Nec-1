import streamlit as st
import pickle
import pandas as pd

st.title("🛒 Purchase Prediction")

try:

    with open(
        "models/purchase_model.pkl",
        "rb"
    ) as file:

        model = pickle.load(file)

    st.markdown(
        """
        Predict the likelihood of a customer making a purchase
        based on customer attributes.
        """
    )

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

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    gender_value = 1 if gender == "Male" else 0

    if st.button("Predict Purchase Behaviour"):

        input_data = pd.DataFrame(
            [[
                age,
                income,
                spending,
                gender_value
            ]],
            columns=[
                "Age",
                "AnnualIncome",
                "SpendingScore",
                "Gender"
            ]
        )

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        probability_percent = round(
            probability * 100,
            2
        )

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success(
                f"Likely to Purchase ({probability_percent}%)"
            )

            st.info(
                """
                Recommended Strategy:

                • Promote premium products

                • Offer loyalty rewards

                • Send personalized offers

                • Target through email campaigns
                """
            )

        else:

            st.warning(
                f"Less Likely to Purchase ({probability_percent}%)"
            )

            st.info(
                """
                Recommended Strategy:

                • Offer discounts

                • Send promotional coupons

                • Re-engage through marketing campaigns

                • Introduce entry-level products
                """
            )

        st.divider()

        st.subheader("Customer Profile")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Age",
            age
        )

        c2.metric(
            "Income",
            f"₹{income:,}"
        )

        c3.metric(
            "Spending Score",
            spending
        )

except FileNotFoundError:

    st.error(
        "Model file not found. Run train_model.py first."
    )