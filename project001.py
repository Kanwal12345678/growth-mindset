import streamlit as st
import pandas as pd
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset App",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .stButton>button {
        background-color: #2e7bcf;
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
    }
    .main-header {
        font-size: 40px;
        color: #2e7bcf;
        text-align: center;
        margin-bottom: 30px;
    }
    .sub-header {
        font-size: 25px;
        color: #1f5c9d;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Navigation")
    page = st.radio(
        "Choose a section:",
        ["Home", "Self Evaluation", "Daily Insights", "Resources"]
    )
    
    st.markdown("---")
    st.markdown("### About Growth Mindset")
    st.write("A growth mindset is the belief that skills and intelligence can evolve with effort, dedication, and constructive feedback.")

# Main content
if page == "Home":
    st.markdown("<h1 class='main-header'>🌱 Foster Your Growth Mindset</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Fixed vs Growth Mindset</h2>", unsafe_allow_html=True)
        st.write("""
        - 🌱 **Growth Mindset**: Believes abilities can be cultivated
        - 🚫 **Fixed Mindset**: Believes abilities are set
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Core Principles</h2>", unsafe_allow_html=True)
        st.write("""
        1. Embrace challenges as opportunities
        2. Learn from constructive criticism
        3. Draw motivation from others' achievements
        4. Persevere through obstacles
        """)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Self Evaluation":
    st.markdown("<h1 class='main-header'>📊 Growth Mindset Self-Evaluation</h1>", unsafe_allow_html=True)
    
    questions = {
        "I believe I can enhance my intelligence over time": 0,
        "I view challenges as opportunities for growth": 0,
        "I accept and learn from feedback": 0,
        "I persist despite difficulties": 0,
        "I find motivation in the success of others": 0
    }
    
    st.write("Rate yourself on the following statements (1-5):")
    for question in questions:
        questions[question] = st.slider(question, 1, 5, 3)
    
    if st.button("Calculate Score"):
        score = sum(questions.values())
        max_score = len(questions) * 5
        percentage = (score / max_score) * 100
        
        st.markdown(f"<div class='info-box'>", unsafe_allow_html=True)
        st.markdown(f"### Your Growth Mindset Score: {percentage:.1f}%")
        
        if percentage >= 80:
            st.success("You have a strong growth mindset! Keep nurturing it!")
        elif percentage >= 60:
            st.info("You're on the right path! There’s still room for improvement.")
        else:
            st.warning("Consider adopting more growth-oriented thinking!")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Daily Insights":
    st.markdown("<h1 class='main-header'>📝 Daily Growth Reflections</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    date = st.date_input("Date")
    challenge = st.text_area("What challenges did you face today?")
    learning = st.text_area("What did you learn from these challenges?")
    tomorrow = st.text_area("How will you apply this learning tomorrow?")
    
    if st.button("Save Reflection"):
        st.success("Reflection saved successfully!")
        st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)

else:  # Resources page
    st.markdown("<h1 class='main-header'>📚 Growth Mindset Resources</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Recommended Books</h2>", unsafe_allow_html=True)
    st.write("""
    - "Mindset: The New Psychology of Success" by Carol S. Dweck
    - "Grit: The Power of Passion and Perseverance" by Angela Duckworth
    - "Atomic Habits" by James Clear
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Daily Practice Tips</h2>", unsafe_allow_html=True)
    st.write("""
    1. Focus on learning goals, not just performance goals
    2. Embrace challenges and view them as opportunities
    3. Practice self-reflection every day
    4. Actively seek feedback and grow from it
    5. Celebrate every small success along the way
    """)
    st.markdown("</div>", unsafe_allow_html=True)
