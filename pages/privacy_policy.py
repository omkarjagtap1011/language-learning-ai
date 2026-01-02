"""
Privacy Policy Page for Language Learning Difficulty Analyzer
"""

import streamlit as st

st.set_page_config(
    page_title="Privacy Policy - Language Learning Difficulty Analyzer",
    page_icon="🔒",
    layout="wide",
)

st.title("🔒 Privacy Policy")

st.markdown("""
**Last Updated: January 3, 2026**

Welcome to the Language Learning Difficulty Analyzer. Your privacy is important to us. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our application.

---

## 1. Information We Collect

### 1.1 Google Account Information
When you sign in with Google, we receive and store the following information from your Google account:
- **Name**: Your display name from your Google profile
- **Email Address**: Your primary email address associated with your Google account
- **Profile Picture**: Your Google profile picture URL (optional)
- **User ID**: A unique identifier for your account

**We do NOT access:**
- Your Google contacts
- Your Google Drive files
- Your Gmail messages
- Your calendar or any other Google services

### 1.2 Personal Information
We may collect additional personal information that you voluntarily provide when using our service, including:
- User preferences and settings
- Learning progress and performance data

### 1.2 Audio Data
When you upload audio files for analysis:
- Audio files are processed temporarily for transcription and analysis
- Processed results (transcriptions, difficulty scores) may be stored to improve your learning experience
- Original audio files are not permanently stored unless you explicitly save them

### 1.3 Usage Data
We automatically collect certain information when you use the application:
- Browser type and version
- Device information
- Session duration and interaction patterns
- Features used within the application

### 1.4 Cookies and Local Storage
We use cookies and local storage to:
- Maintain your session and authentication state
- Remember your preferences and settings
- Track your learning progress

---

## 2. How We Use Your Information

We use the collected information for the following purposes:

- **Provide Services**: To process audio files, generate transcriptions, and analyze difficulty levels
- **Personalization**: To customize your learning experience based on your progress and preferences
- **Improvement**: To improve our algorithms, user interface, and overall service quality
- **Communication**: To respond to your inquiries and provide support
- **Analytics**: To understand usage patterns and optimize the application

---

## 3. Data Storage and Security

### 3.1 Data Storage
- User data is stored securely using industry-standard encryption
- Audio files are processed in temporary storage and deleted after processing unless explicitly saved
- Learning progress data is stored to provide continuity in your learning journey

### 3.2 Security Measures
We implement appropriate technical and organizational measures to protect your data:
- Encryption in transit (HTTPS/TLS)
- Secure authentication mechanisms
- Regular security assessments
- Access controls and monitoring

---

## 4. Data Sharing and Disclosure

We do not sell, trade, or rent your personal information to third parties. We may share your information in the following circumstances:

- **Service Providers**: With trusted third-party services that assist in operating our application (e.g., cloud hosting, analytics)
- **Legal Requirements**: When required by law, court order, or governmental authority
- **Safety**: To protect the rights, property, or safety of our users or others
- **Consent**: With your explicit consent for specific purposes

---

## 5. Third-Party Services

Our application may use third-party services for:
- Cloud storage and processing
- Speech recognition and transcription
- Analytics and performance monitoring

These services have their own privacy policies, and we encourage you to review them.

---

## 6. Your Rights and Choices

You have the following rights regarding your personal data:

- **Access**: Request a copy of your personal data
- **Correction**: Request correction of inaccurate data
- **Deletion**: Request deletion of your personal data
- **Portability**: Request your data in a portable format
- **Opt-out**: Opt out of certain data collection practices

To exercise these rights, please contact us using the information provided below.

---

## 7. Children's Privacy

Our service is not intended for children under 13 years of age. We do not knowingly collect personal information from children under 13. If you believe we have collected such information, please contact us immediately.

---

## 8. International Data Transfers

Your information may be transferred to and processed in countries other than your country of residence. We ensure appropriate safeguards are in place for such transfers in compliance with applicable data protection laws.

---

## 9. Data Retention

We retain your personal data for as long as necessary to:
- Provide our services
- Comply with legal obligations
- Resolve disputes
- Enforce our agreements

You may request deletion of your data at any time, subject to legal retention requirements.

---

## 10. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by:
- Posting the new Privacy Policy on this page
- Updating the "Last Updated" date at the top

We encourage you to review this Privacy Policy periodically for any changes.

---

## 11. Contact Us

If you have any questions or concerns about this Privacy Policy or our data practices, please contact us:

- **Email**: privacy@languagelearning.app
- **Subject Line**: Privacy Policy Inquiry

---

## 12. Consent

By using the Language Learning Difficulty Analyzer, you consent to the collection, use, and sharing of your information as described in this Privacy Policy.

---

*Thank you for trusting us with your language learning journey. We are committed to protecting your privacy and providing a secure learning environment.*
""")

# Back button
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("← Back to Main App", use_container_width=True):
        st.switch_page("app.py")

# Footer
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    Made with ❤️ for language learners | Powered by Streamlit
</div>
""", unsafe_allow_html=True)
