import streamlit as st
import pandas as pd
from expense import Expense
from utils import add_expense, view_expenses
from analytics import analyze_expenses_df
from ai_insights import generate_insights
from finance_api import get_stock_data
from db import create_table

create_table()

st.title("💰 Smart Expense Tracker AI")

menu = st.sidebar.selectbox(
    "Menu", ["Add Expense", "View Expenses", "Analytics", "AI Insights", "Finance"]
)

def html_table(df):
    return df.to_html(index=False)

def html_bar_chart(data_dict):
    if not data_dict:
        return "<p>No data to chart</p>"
    max_val = max(data_dict.values())
    bars = ""
    for label, value in data_dict.items():
        width = (value / max_val) * 100 if max_val else 0
        bars += (
            f'<div style="margin:6px 0;">'
            f'<span style="display:inline-block;width:120px;font-weight:bold;">{label}</span>'
            f'<div style="display:inline-block;width:{width:.1f}%;background:#4CAF50;height:20px;vertical-align:middle;margin-right:8px;"></div>'
            f'<span>{value:.2f}</span>'
            f'</div>'
        )
    return f'<div style="font-family:sans-serif;">{bars}</div>'

def html_line_table(df, max_rows=20):
    if df.empty:
        return "<p>No data</p>"
    df = df.tail(max_rows)
    return df.to_html(index=False)

if menu == "Add Expense":
    title = st.text_input("Title")
    amount = st.number_input("Amount")
    category = st.text_input("Category")
    date = st.date_input("Date")

    if st.button("Add"):
        exp = Expense(title, amount, category, str(date))
        add_expense(exp)
        st.success("Expense Added!")

elif menu == "View Expenses":
    data = view_expenses()
    if data:
        df = pd.DataFrame(data, columns=["ID", "Title", "Amount", "Category", "Date"])
        st.markdown(html_table(df), unsafe_allow_html=True)
    else:
        st.info("No expenses found.")

elif menu == "Analytics":
    df = analyze_expenses_df()
    if not df.empty:
        st.markdown(html_table(df), unsafe_allow_html=True)
        st.subheader("Spending by Category")
        category_sums = df.groupby("category")["amount"].sum().to_dict()
        st.markdown(html_bar_chart(category_sums), unsafe_allow_html=True)
    else:
        st.info("No data available")

elif menu == "AI Insights":
    df = analyze_expenses_df()
    if not df.empty:
        insights = generate_insights(df)
        st.text(insights)
    else:
        st.warning("No data available")

elif menu == "Finance":
    ticker = st.text_input("Enter Stock (e.g., AAPL)")
    if st.button("Fetch"):
        df = get_stock_data(ticker)
        if not df.empty:
            st.markdown(html_line_table(df[["Close"]].reset_index()), unsafe_allow_html=True)
        else:
            st.warning("No data fetched")
