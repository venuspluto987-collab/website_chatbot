import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_excel("chatbot_excel_data.xlsx")

# Function to find answer
def find_answer(question):
    question = question.lower()

    for _, row in df.iterrows():
        excel_q = str(row["Question"]).lower()
        if excel_q in question:
            return row["Answer"]

    return "Sorry, I don't know this answer."

# Streamlit UI
st.title("🤖 Excel AI Chatbot")

user_question = st.text_input("Ask me anything:")

if user_question:
    answer = find_answer(user_question)
    st.write("**Bot:**", answer)
