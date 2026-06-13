import streamlit as st
import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.title("📄 Business Report Generator")

try:

    df = pd.read_csv(
        "data/customers_clustered.csv"
    )

    total_customers = len(df)

    avg_income = round(
        df["AnnualIncome"].mean(),
        2
    )

    avg_spending = round(
        df["SpendingScore"].mean(),
        2
    )

    st.subheader("Report Summary")

    st.write(
        "Total Customers:",
        total_customers
    )

    st.write(
        "Average Income:",
        avg_income
    )

    st.write(
        "Average Spending:",
        avg_spending
    )

    st.markdown("---")

    excel_data = df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download Excel Report",
        excel_data,
        "Customer_Report.csv",
        "text/csv"
    )

    if st.button(
        "Generate PDF Report"
    ):

        temp_pdf = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        pdf = SimpleDocTemplate(
            temp_pdf.name
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "AI Customer Analytics Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        content.append(
            Paragraph(
                f"Total Customers: {total_customers}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average Income: {avg_income}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average Spending Score: {avg_spending}",
                styles["Normal"]
            )
        )

        pdf.build(content)

        with open(
            temp_pdf.name,
            "rb"
        ) as file:

            st.download_button(
                "⬇ Download PDF Report",
                file,
                "AI_Customer_Report.pdf",
                "application/pdf"
            )

except FileNotFoundError:

    st.error(
        "Run train_model.py first."
    )