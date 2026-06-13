import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Customer Analytics Dashboard")

try:
    df = pd.read_csv("data/customers_clustered.csv")

    # -----------------------
    # KPI SECTION
    # -----------------------

    total_customers = len(df)
    avg_income = round(df["AnnualIncome"].mean(), 2)
    avg_spending = round(df["SpendingScore"].mean(), 2)

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Customers", total_customers)
    c2.metric("Average Income", f"₹{avg_income:,.0f}")
    c3.metric("Average Spending Score", avg_spending)

    st.divider()

    # -----------------------
    # SEARCH + FILTER
    # -----------------------

    search = st.text_input(
        "🔍 Search Customer ID"
    )

    if search:
        df = df[
            df["CustomerID"].astype(str).str.contains(search)
        ]

    cluster_filter = st.selectbox(
        "Filter Customer Segment",
        ["All"] + sorted(df["Cluster"].unique().tolist())
    )

    if cluster_filter != "All":
        df = df[df["Cluster"] == cluster_filter]

    # -----------------------
    # CUSTOMER TABLE
    # -----------------------

    st.subheader("📋 Customer Data")

    st.dataframe(
        df,
        width="stretch"
    )

    st.download_button(
        "⬇ Download Customer Data",
        df.to_csv(index=False),
        "customers_filtered.csv",
        "text/csv"
    )

    st.divider()

    # -----------------------
    # BUSINESS INSIGHTS
    # -----------------------

    st.header("📈 Business Insights")

    col1, col2 = st.columns(2)

    # Cluster Distribution

    with col1:

        cluster_count = (
            df["Cluster"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        cluster_count.columns = [
            "Cluster",
            "Customers"
        ]

        fig_cluster_count = px.bar(
            cluster_count,
            x="Cluster",
            y="Customers",
            title="Customer Distribution by Segment"
        )

        st.plotly_chart(
            fig_cluster_count,
            width="stretch"
        )

    # Average Spending

    with col2:

        spending_cluster = (
            df.groupby("Cluster")["SpendingScore"]
            .mean()
            .reset_index()
        )

        fig_spending_cluster = px.bar(
            spending_cluster,
            x="Cluster",
            y="SpendingScore",
            title="Average Spending by Segment"
        )

        st.plotly_chart(
            fig_spending_cluster,
            width="stretch"
        )

    # -----------------------
    # SECOND ROW
    # -----------------------

    col3, col4 = st.columns(2)

    # Average Income

    with col3:

        income_cluster = (
            df.groupby("Cluster")["AnnualIncome"]
            .mean()
            .reset_index()
        )

        fig_income_cluster = px.bar(
            income_cluster,
            x="Cluster",
            y="AnnualIncome",
            title="Average Income by Segment"
        )

        st.plotly_chart(
            fig_income_cluster,
            width="stretch"
        )

    # High Value Customer Analysis

    with col4:

        high_value = df[
            (df["AnnualIncome"] > 70000)
            &
            (df["SpendingScore"] > 70)
        ]

        normal_customers = len(df) - len(high_value)

        hv_df = pd.DataFrame({
            "Type": [
                "High Value",
                "Normal"
            ],
            "Count": [
                len(high_value),
                normal_customers
            ]
        })

        fig_hv = px.pie(
            hv_df,
            names="Type",
            values="Count",
            title="High Value Customer Analysis"
        )

        st.plotly_chart(
            fig_hv,
            width="stretch"
        )

    st.divider()

    # -----------------------
    # MAIN ML VISUALIZATION
    # -----------------------

    st.header("🤖 Customer Segmentation")

    fig_cluster = px.scatter(
        df,
        x="AnnualIncome",
        y="SpendingScore",
        color=df["Cluster"].astype(str),
        hover_data=[
            "CustomerID",
            "Age"
        ],
        title="Income vs Spending Score Segmentation"
    )

    st.plotly_chart(
        fig_cluster,
        width="stretch"
    )

    st.divider()

    # -----------------------
    # SUPPORTING ANALYTICS
    # -----------------------

    st.header("📊 Additional Analytics")

    col5, col6 = st.columns(2)

    with col5:

        fig_income = px.histogram(
            df,
            x="AnnualIncome",
            nbins=20,
            title="Income Distribution"
        )

        st.plotly_chart(
            fig_income,
            width="stretch"
        )

    with col6:

        fig_spending = px.histogram(
            df,
            x="SpendingScore",
            nbins=20,
            title="Spending Score Distribution"
        )

        st.plotly_chart(
            fig_spending,
            width="stretch"
        )

    # -----------------------
    # SMALL GENDER PIE
    # -----------------------

    st.subheader("Gender Distribution")

    gender_col1, gender_col2 = st.columns([1, 2])

    with gender_col1:

        fig_gender = px.pie(
            df,
            names="Gender"
        )

        st.plotly_chart(
            fig_gender,
            width="stretch"
        )

    with gender_col2:

        st.info(
            """
            Gender distribution is shown for demographic reference.

            Business decisions should primarily focus on:

            • Customer Segments

            • Spending Behaviour

            • High Value Customers

            • Churn Risk

            """
        )

    st.divider()

    # -----------------------
    # TOP CUSTOMERS
    # -----------------------

    st.subheader("🏆 Top 5 Customers")

    top5 = df.sort_values(
        "SpendingScore",
        ascending=False
    ).head(5)

    st.dataframe(
        top5,
        width="stretch"
    )

    # -----------------------
    # CLUSTER SUMMARY
    # -----------------------

    st.subheader("📑 Segment Summary")

    cluster_summary = (
        df.groupby("Cluster")
        [
            [
                "AnnualIncome",
                "SpendingScore"
            ]
        ]
        .mean()
        .round(2)
    )

    st.dataframe(
        cluster_summary,
        width="stretch"
    )

    # -----------------------
    # HIGH VALUE TABLE
    # -----------------------

    st.subheader("⭐ High Value Customers")

    st.dataframe(
        high_value,
        width="stretch"
    )

except FileNotFoundError:

    st.error(
        "customers_clustered.csv not found. Run train_model.py first."
    )