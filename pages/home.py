"""
Public Homepage for Language Learning Difficulty Analyzer
This page is visible without requiring users to log in and meets app verification requirements.
"""

import streamlit as st

st.set_page_config(
    page_title="Language Learning Difficulty Analyzer - Home",
    page_icon="🎙️",
    layout="wide",
)

# Hero Section
st.markdown("""
<div style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 60px 40px;
    border-radius: 20px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
">
    <h1 style="color: white; font-size: 2.8em; margin-bottom: 15px; font-weight: 700;">
        🎙️ Language Learning Difficulty Analyzer
    </h1>
    <p style="color: rgba(255,255,255,0.95); font-size: 1.3em; max-width: 800px; margin: 0 auto 25px auto; line-height: 1.6;">
        Empowering language learners with AI-powered audio analysis to master Indic languages at their own pace
    </p>
    <a href="/app" target="_self" style="
        display: inline-block;
        background: white;
        color: #667eea;
        padding: 15px 40px;
        border-radius: 30px;
        font-size: 1.1em;
        font-weight: 600;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s;
    ">Get Started →</a>
</div>
""", unsafe_allow_html=True)

# About Our App Section
st.markdown("## 🎯 About Our Application")

st.markdown("""
The **Language Learning Difficulty Analyzer** is a comprehensive educational tool designed to help learners 
master Indic languages (particularly Hindi) through intelligent audio analysis and personalized practice.

Our application is developed by language learning enthusiasts and researchers committed to making 
language education more accessible and effective through technology.
""")

st.divider()

# Core Features Section
st.markdown("## ✨ Core Features & Functionality")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎵 Audio Processing Pipeline
    - **Voice Activity Detection (VAD)**: Automatically segments audio into dialogue chunks
    - **Speech Transcription**: Converts spoken Indic languages to text using state-of-the-art models
    - **Sentence Alignment**: Maps transcribed sentences to their exact timestamps in the audio
    
    ### 📊 Difficulty Analysis
    - **Readability Metrics (RH1 & RH2)**: Measures text complexity for Indic languages
    - **Sentence Length Analysis**: Evaluates sentence complexity by word count
    - **Combined Scoring**: Intelligent difficulty ratings to guide your learning path
    """)

with col2:
    st.markdown("""
    ### 🎯 Interactive Practice
    - **Spaced Repetition System (FSRS)**: Scientifically-proven learning intervals
    - **Flashcard Practice**: Review sentences with audio, transliteration, and translation
    - **Progress Tracking**: Monitor your learning journey with detailed statistics
    
    ### 🎮 Translation Game
    - **Adaptive Difficulty**: Glicko-2 rating system adjusts to your skill level
    - **Real-time Feedback**: Instant evaluation of your translation attempts
    - **Skill-based Matching**: Practice with sentences matched to your ability
    """)

st.divider()

# Data Usage Section - Required for App Verification
st.markdown("## 🔐 How We Use Your Data")

st.markdown("""
<div style="
    background: #f8f9fa;
    padding: 30px;
    border-radius: 15px;
    border-left: 5px solid #667eea;
    margin: 20px 0;
">
    <h3 style="color: #333; margin-top: 0;">Transparency in Data Collection</h3>
    <p style="color: #555; line-height: 1.8;">
        We believe in complete transparency about how your data is used. Here's exactly what we collect and why:
    </p>
</div>
""", unsafe_allow_html=True)

data_col1, data_col2 = st.columns(2)

with data_col1:
    st.markdown("""
    ### 📧 Information We Request
    
    **Google Sign-In Data:**
    - **Name**: To personalize your learning experience
    - **Email Address**: For account identification and communication
    - **Profile Picture**: To display in your user profile
    
    **Learning Data (Stored Securely):**
    - Practice session results and progress
    - Difficulty ratings and annotations you provide
    - Translation game scores and skill ratings
    """)

with data_col2:
    st.markdown("""
    ### 🎯 Why We Need This Data
    
    **Personalization:**
    - Track your learning progress across sessions
    - Provide spaced repetition scheduling tailored to you
    - Adjust difficulty based on your performance
    
    **Service Improvement:**
    - Improve our difficulty assessment algorithms
    - Enhance transcription accuracy
    - Better understand learner needs
    """)

st.info("""
🔒 **Our Privacy Commitment**
- We **never sell** your personal data to third parties
- Audio files are processed temporarily and **not permanently stored** unless you save them
- You can **request deletion** of your data at any time
- All data transmission is **encrypted** using HTTPS/TLS
""")

st.divider()

# Technologies Section
st.markdown("## 🛠️ Technologies We Use")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    ### Speech Processing
    - WebRTC VAD for voice detection
    - Indic Conformer models for transcription
    - Advanced punctuation restoration
    """)

with tech_col2:
    st.markdown("""
    ### Machine Learning
    - Custom readability metrics for Indic languages
    - Glicko-2 adaptive rating system
    - FSRS spaced repetition algorithm
    """)

with tech_col3:
    st.markdown("""
    ### Platform
    - Streamlit for interactive UI
    - Secure cloud storage
    - Google OAuth authentication
    """)

st.divider()

# Getting Started Section
st.markdown("## 🚀 Getting Started")

st.markdown("""
<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 30px 0;">
    <div style="
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        width: 200px;
    ">
        <div style="font-size: 2.5em; margin-bottom: 10px;">1️⃣</div>
        <h4 style="margin: 10px 0;">Sign In</h4>
        <p style="color: #666; font-size: 0.9em;">Use your Google account for secure access</p>
    </div>
    <div style="
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        width: 200px;
    ">
        <div style="font-size: 2.5em; margin-bottom: 10px;">2️⃣</div>
        <h4 style="margin: 10px 0;">Load Content</h4>
        <p style="color: #666; font-size: 0.9em;">Upload audio or load existing analysis results</p>
    </div>
    <div style="
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        width: 200px;
    ">
        <div style="font-size: 2.5em; margin-bottom: 10px;">3️⃣</div>
        <h4 style="margin: 10px 0;">Practice</h4>
        <p style="color: #666; font-size: 0.9em;">Learn with flashcards and translation games</p>
    </div>
    <div style="
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        width: 200px;
    ">
        <div style="font-size: 2.5em; margin-bottom: 10px;">4️⃣</div>
        <h4 style="margin: 10px 0;">Track Progress</h4>
        <p style="color: #666; font-size: 0.9em;">Monitor your improvement over time</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Call to Action
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 30px 0;">
        <h2>Ready to Start Learning?</h2>
        <p style="color: #666; margin-bottom: 20px;">
            Sign in with your Google account to access all features and begin your language learning journey.
        </p>
        <a href="/app" target="_self" style="
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 50px;
            border-radius: 30px;
            font-size: 1.1em;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        ">Sign In to Get Started</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Legal Links Section - Required for App Verification
st.markdown("## 📋 Legal Information")

legal_col1, legal_col2, legal_col3 = st.columns(3)

with legal_col1:
    st.markdown("""
    ### [🔒 Privacy Policy](/privacy_policy)
    Learn how we collect, use, and protect your personal information. 
    We are committed to safeguarding your privacy.
    """)

with legal_col2:
    st.markdown("""
    ### [📜 Terms of Service](/terms_of_service)
    Read our terms and conditions for using the Language Learning 
    Difficulty Analyzer application.
    """)

with legal_col3:
    st.markdown("""
    ### 📧 Contact Us
    Have questions or concerns?
    
    **Email:** support@languagelearning.app
    """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p style="margin-bottom: 10px;">
        <strong>Language Learning Difficulty Analyzer</strong><br>
        Empowering learners to master Indic languages through AI-powered analysis
    </p>
    <p>
        Made with ❤️ for language learners | Powered by Streamlit<br>
        <a href="/privacy_policy" target="_self" style="color: gray; text-decoration: none;">Privacy Policy</a> | 
        <a href="/terms_of_service" target="_self" style="color: gray; text-decoration: none;">Terms of Service</a>
    </p>
    <p style="font-size: 0.85em; margin-top: 15px;">
        © 2026 Language Learning Difficulty Analyzer. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)
