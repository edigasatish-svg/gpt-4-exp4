import streamlit as st

# Configure the web page
st.set_page_config(page_title="Personalized AI Recommender", layout="centered")

st.title("🤖 Personalized Recommendation System")
st.markdown("Enter your profile below to get personalized recommendations based on AI analysis.")

# Initialize memory (session state) for our web app
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'feedback_submitted' not in st.session_state:
    st.session_state.feedback_submitted = False

# Sidebar for User Profile Input
with st.sidebar:
    st.header("👤 User Profile")
    name = st.text_input("Name", "Arun")
    age = st.text_input("Age", "20")
    field = st.text_input("Field", "Computer Science")
    interests = st.text_input("Interests", "AI, Python")
    level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
    preference = st.selectbox("Preferred Type", ["Practical", "Theoretical", "Project-based"])
    goal = st.text_input("Goal", "Learn AI")
    
    # Button to submit profile
    generate_btn = st.button("Generate Recommendations", type="primary")

# Action when the button is clicked
if generate_btn:
    st.session_state.feedback_submitted = False
    with st.spinner("Analyzing preferences using GPT-4 Logic..."):
        # Simulated LLM generation based on profile
        st.session_state.recommendations = [
            {"Rank": 1, "Recommendation": f"Python for {interests.split(',')[0] if ',' in interests else interests}", "Reason": f"Perfect match for your interest in {interests}.", "Score": "95%"},
            {"Rank": 2, "Recommendation": "Machine Learning Basics", "Reason": f"Suitable for {level} level learners.", "Score": "92%"},
            {"Rank": 3, "Recommendation": "Generative AI", "Reason": f"Highly relevant to current tech trends in {field}.", "Score": "88%"},
            {"Rank": 4, "Recommendation": "Data Science Fundamentals", "Reason": f"Combines {interests} and Data.", "Score": "85%"},
            {"Rank": 5, "Recommendation": "Deep Learning Basics", "Reason": "Natural progression after ML.", "Score": "80%"}
        ]

# Display initial recommendations
if st.session_state.recommendations is not None and not st.session_state.feedback_submitted:
    st.success(f"Hello {name}! Here are your personalized recommendations:")
    
    # Print out the recommendations beautifully
    for rec in st.session_state.recommendations:
        st.markdown(f"### {rec['Rank']}. {rec['Recommendation']} *(Score: {rec['Score']})*")
        st.info(f"**Reason:** {rec['Reason']}")
        
    st.divider()
    
    # Feedback Module
    st.subheader("🔄 Refine Results")
    feedback = st.text_input("Provide feedback to refine recommendations (e.g., 'I am more interested in AI than Web Dev')")
    
    if st.button("Update Recommendations"):
        st.session_state.feedback_submitted = True
        st.session_state.feedback_text = feedback
        st.rerun() # Refresh page

# Display updated recommendations after feedback
if st.session_state.feedback_submitted:
    st.warning(f"**Feedback Received:** *{st.session_state.feedback_text}*")
    st.success("✅ Recommendations Updated based on your feedback!")
    
    # Updated recommendations simulating LLM interpreting feedback
    updated_recs = [
            {"Rank": 1, "Recommendation": "Advanced Artificial Intelligence", "Reason": "Adjusted heavily towards AI based on your specific feedback.", "Score": "98%"},
            {"Rank": 2, "Recommendation": "Deep Learning Specialization", "Reason": "More focused on advanced AI topics.", "Score": "95%"},
            {"Rank": 3, "Recommendation": "Computer Vision", "Reason": "Highly requested AI subfield.", "Score": "90%"},
            {"Rank": 4, "Recommendation": "NLP with Transformers", "Reason": "Core component of Generative AI.", "Score": "88%"},
            {"Rank": 5, "Recommendation": "AI Capstone Project", "Reason": f"Practical implementation for a {level} user.", "Score": "85%"}
    ]
    
    for rec in updated_recs:
        st.markdown(f"### {rec['Rank']}. {rec['Recommendation']} *(Score: {rec['Score']})*")
        st.info(f"**Reason:** {rec['Reason']}")
