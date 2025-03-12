import streamlit as st
import random 
import time 

st.title("📝 Quiz Application By Sadiq")

questions = [
    {
        "question": "What is the national flower of Pakistan?",
        "options": ["Rose", "Tulip", "Jasmine", "Sunflower"],
        "answer": "Jasmine",
    },
    {
        "question": "Which river is the longest in Pakistan?",
        "options": ["Jhelum", "Chenab", "Indus", "Ravi"],
        "answer": "Indus",
    },
    {
        "question": "When did Pakistan become an independent country?",
        "options": ["1945", "1947", "1950", "1965"],
        "answer": "1947",
    },
    {
        "question": "Who was the first Prime Minister of Pakistan?",
        "options": ["Liaquat Ali Khan", "Benazir Bhutto", "Zulfikar Ali Bhutto", "Ayub Khan"],
        "answer": "Liaquat Ali Khan",
    },
    {
        "question": "Which is the highest peak in Pakistan?",
        "options": ["Nanga Parbat", "K2", "Rakaposhi", "Broad Peak"],
        "answer": "K2",
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Lion", "Tiger", "Markhor", "Elephant"],
        "answer": "Markhor",
    },
    {
        "question": "Which sea borders Pakistan to the south?",
        "options": ["Red Sea", "Arabian Sea", "Bay of Bengal", "Caspian Sea"],
        "answer": "Arabian Sea",
    },
    {
        "question": "Which Pakistani scientist won the Nobel Prize in Physics?",
        "options": ["Dr. Abdul Qadeer Khan", "Abdus Salam", "Salimuzzaman Siddiqui", "Atta-ur-Rahman"],
        "answer": "Abdus Salam",
    },
    {
        "question": "Which city is known as the Heart of Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Multan"],
        "answer": "Lahore",
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Hockey", "Football", "Squash"],
        "answer": "Hockey",
    },
]



if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    time.sleep(5)

    st.session_state.current_question = random.choice(questions)
 
    st.rerun()