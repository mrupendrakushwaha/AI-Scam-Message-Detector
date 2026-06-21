import streamlit as st
import joblib

model = joblib.load("scam_detector.pkl")

st.title("🛡 AI Scam Message Detector")

msg = st.text_area("Paste SMS / WhatsApp Message")
if st.button("Analyze"):

    suspicious_words = [
        "bit.ly",
        "otp",
        "password",
        "kyc",
        "verify",
        "click",
        "urgent",
        "bank account",
        "upi",
        "reward",
        "won"
    ]

    msg_lower = msg.lower()

    keyword_score = 0

    for word in suspicious_words:
        if word in msg_lower:
            keyword_score += 5

    pred = model.predict([msg])[0]
    prob = model.predict_proba([msg])

    scam_score = round(prob[0][1] * 100, 2)
    scam_score = min(scam_score + keyword_score, 100)

    if pred == 1 or keyword_score > 0:
        st.error(f"⚠ Scam Detected ({scam_score}%)")
    else:
        st.success(f"✅ Genuine Message ({100-scam_score}%)")

