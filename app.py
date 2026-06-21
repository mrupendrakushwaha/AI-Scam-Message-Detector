import streamlit as st
import joblib

model = joblib.load("scam_detector.pkl")

st.title("🛡 AI Scam Message Detector")

msg = st.text_area("Paste SMS / WhatsApp Message")

if st.button("Analyze"):

    pred = model.predict([msg])[0]
    prob = model.predict_proba([msg])

    scam_score = round(prob[0][1] * 100, 2)

    if pred == 1:
        st.error(f"⚠ Scam Detected ({scam_score}%)")
    else:
        st.success(f"✅ Genuine Message ({100-scam_score}%)")
