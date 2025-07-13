import streamlit as st
import random

# Riddles and answers
riddles = [
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
    {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
]

# Score tracker
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🔥 Phoenix Riddle Chatbot")

# Upload logo
st.image("A_digital_vector_illustration_of_a_phoenix_emblem_.png", width=150)

st.markdown("**Type your answer below:**")

# Pick a riddle
if "current_riddle" not in st.session_state:
    st.session_state.current_riddle = random.choice(riddles)

riddle = st.session_state.current_riddle
st.write("🤖 Riddle: " + riddle["question"])

user_answer = st.text_input("Your Answer:")

if st.button("Submit"):
    if user_answer.lower().strip() == riddle["answer"]:
        st.success("Correct! 🔥")
        st.session_state.score += 1
        st.balloons()
    else:
        st.error(f"Wrong! 😢 The answer was: {riddle['answer']}")

    # Ask another
    st.session_state.current_riddle = random.choice(riddles)

st.write(f"Your Score: **{st.session_state.score}**")
