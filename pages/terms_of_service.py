"""
Terms of Service Page for Language Learning Difficulty Analyzer
"""

import streamlit as st

st.set_page_config(
    page_title="Terms of Service - Language Learning Difficulty Analyzer",
    page_icon="📜",
    layout="wide",
)

st.title("📜 Terms of Service")

st.markdown("""
**Last Updated: January 3, 2026**

Welcome to the Language Learning Difficulty Analyzer. Please read these Terms of Service ("Terms") carefully before using our application.

---

## 1. Acceptance of Terms

By accessing or using the Language Learning Difficulty Analyzer ("Service"), you agree to be bound by these Terms. If you do not agree to these Terms, please do not use the Service.

---

## 2. Description of Service

The Language Learning Difficulty Analyzer is an educational tool that:
- Analyzes audio recordings to identify sentence difficulty levels
- Provides transcription and transliteration services for Indic languages
- Offers interactive practice and translation exercises
- Tracks learning progress and provides personalized recommendations

---

## 3. User Accounts

### 3.1 Account Creation
- You may be required to create an account to access certain features
- You must provide accurate and complete information during registration
- You are responsible for maintaining the confidentiality of your account credentials

### 3.2 Account Responsibilities
- You are responsible for all activities that occur under your account
- You must notify us immediately of any unauthorized use of your account
- We reserve the right to suspend or terminate accounts that violate these Terms

---

## 4. Acceptable Use

### 4.1 Permitted Use
You may use the Service for:
- Personal language learning and educational purposes
- Analyzing audio content for which you have appropriate rights
- Academic and research purposes in compliance with applicable laws

### 4.2 Prohibited Use
You agree NOT to:
- Upload content that infringes on intellectual property rights
- Use the Service for any illegal or unauthorized purpose
- Attempt to gain unauthorized access to the Service or its systems
- Interfere with or disrupt the Service or servers
- Use automated systems or bots to access the Service without permission
- Upload malicious content, viruses, or harmful code
- Harass, abuse, or harm other users
- Misrepresent your identity or affiliation
- Resell or redistribute the Service without authorization

---

## 5. Intellectual Property

### 5.1 Our Content
- The Service, including its design, features, and content, is protected by copyright, trademark, and other intellectual property laws
- You may not copy, modify, distribute, or create derivative works without our express written permission

### 5.2 Your Content
- You retain ownership of content you upload (audio files, text, etc.)
- By uploading content, you grant us a non-exclusive, worldwide license to process and analyze it for providing the Service
- You represent that you have the necessary rights to upload and share your content

### 5.3 Feedback
Any feedback, suggestions, or ideas you provide about the Service may be used by us without any obligation to compensate you.

---

## 6. Third-Party Services

### 6.1 Integration
The Service may integrate with third-party services for:
- Speech recognition and transcription
- Cloud storage and processing
- Authentication services

### 6.2 Third-Party Terms
Your use of third-party services is subject to their respective terms and policies. We are not responsible for third-party services' content, privacy practices, or availability.

---

## 7. Disclaimer of Warranties

THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO:
- Warranties of merchantability or fitness for a particular purpose
- Warranties that the Service will be uninterrupted, error-free, or secure
- Warranties regarding the accuracy or reliability of results

We do not guarantee that:
- Transcriptions will be 100% accurate
- Difficulty assessments will perfectly match your learning needs
- The Service will meet all your requirements

---

## 8. Limitation of Liability

TO THE MAXIMUM EXTENT PERMITTED BY LAW:
- We shall not be liable for any indirect, incidental, special, consequential, or punitive damages
- Our total liability shall not exceed the amount you paid for the Service in the past 12 months (or $100 if you haven't paid anything)
- We are not liable for any loss of data, profits, or business opportunities

---

## 9. Indemnification

You agree to indemnify and hold harmless the Language Learning Difficulty Analyzer, its operators, affiliates, and employees from any claims, damages, losses, or expenses (including legal fees) arising from:
- Your use of the Service
- Your violation of these Terms
- Your violation of any third-party rights
- Content you upload or share through the Service

---

## 10. Modifications to Service and Terms

### 10.1 Service Changes
We reserve the right to:
- Modify, suspend, or discontinue any part of the Service at any time
- Add or remove features without prior notice
- Update pricing for premium features (if applicable)

### 10.2 Terms Changes
We may update these Terms from time to time. We will notify you of material changes by:
- Posting updated Terms with a new "Last Updated" date
- Providing notice through the Service

Continued use of the Service after changes constitutes acceptance of the new Terms.

---

## 11. Termination

### 11.1 By You
You may stop using the Service at any time. You may request account deletion by contacting us.

### 11.2 By Us
We may terminate or suspend your access to the Service:
- For violation of these Terms
- For illegal or harmful activities
- For extended periods of inactivity
- At our discretion, with or without cause

### 11.3 Effect of Termination
Upon termination:
- Your right to use the Service will immediately cease
- We may delete your account and associated data
- Provisions that by their nature should survive will remain in effect

---

## 12. Governing Law and Disputes

### 12.1 Governing Law
These Terms shall be governed by and construed in accordance with applicable laws, without regard to conflict of law principles.

### 12.2 Dispute Resolution
Any disputes arising from these Terms or the Service shall be resolved through:
1. Good-faith negotiation between the parties
2. Mediation, if negotiation fails
3. Binding arbitration or court proceedings as a last resort

---

## 13. General Provisions

### 13.1 Entire Agreement
These Terms, together with our Privacy Policy, constitute the entire agreement between you and us regarding the Service.

### 13.2 Severability
If any provision of these Terms is found invalid or unenforceable, the remaining provisions shall continue in full force and effect.

### 13.3 Waiver
Our failure to enforce any right or provision of these Terms shall not constitute a waiver of such right or provision.

### 13.4 Assignment
You may not assign or transfer your rights under these Terms without our prior written consent.

---

## 14. Contact Us

If you have any questions about these Terms of Service, please contact us:

- **Email**: legal@languagelearning.app
- **Subject Line**: Terms of Service Inquiry

---

## 15. Acknowledgment

By using the Language Learning Difficulty Analyzer, you acknowledge that you have read, understood, and agree to be bound by these Terms of Service.

---

*Thank you for using the Language Learning Difficulty Analyzer. We hope it helps you on your language learning journey!*
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
