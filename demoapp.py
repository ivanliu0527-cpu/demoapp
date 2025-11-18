import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Personl Expense Tracker")

if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

with st.form("expense_form", clear_on_submit=True):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_input("Description")
    
    add_expense_button = st.form_submit_button("Add Expense")
    
    if add_expense_button:
        new_expense = pd.DataFrame({
            "Date": {date},
            "Category": {category},
            "Amount": {amount},
            "Description": {description}
            })
        
        st.session_state.expenses = st.session_state.expenses.append(new_expense, ignore_index=True)
        st.success("Expense added!")

if not st.session_state.expenses.empty:
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)
    
    st.subheader("Summary")
    total_spent = st.session_state.expenses["Amount"].sum()
    st.write(f"Total Spent: ${total_spent:.2f}")
    
    # Expense by Category
    st.subheader("Expense by Category")
    category_expense = st.session_state.expenses.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.pie(category_expense["Amount"], labels=category_expense["Category"], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig)
