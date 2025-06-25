import streamlit as st
from PIL import Image
import easyocr
import cv2
import numpy as np
from datetime import datetime
import os
import urllib.request

# ------------------ Streamlit Page Setup ------------------
st.set_page_config(page_title="FaceIQ", layout="centered")
st.title("📷 FaceIQ")
st.subheader("Smart Age & Identity Verification System")

# ------------------ Haar Cascade Setup ------------------
CASCADE_URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
CASCADE_FILE = "haarcascade_frontalface_default.xml"

if not os.path.exists(CASCADE_FILE):
    urllib.request.urlretrieve(CASCADE_URL, CASCADE_FILE)

face_cascade = cv2.CascadeClassifier(CASCADE_FILE)

# ------------------ Function: Extract DOB ------------------
def extract_dob_easyocr(image):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(np.array(image))
    for _, text, _ in result:
        if "DOB" in text or "Birth" in text:
            return ''.join([c for c in text if c.isdigit() or c == '/'])
    return "Not Found"

# ------------------ Function: Calculate Age ------------------
def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    except Exception as e:
        return None

# ------------------ Function: Face Match ------------------
def face_match(img1, img2):
    def extract_face(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            return cv2.resize(img[y:y+h, x:x+w], (100, 100))
        return None

    face1 = extract_face(img1)
    face2 = extract_face(img2)

    if face1 is None or face2 is None:
        return 0.0

    mse = np.mean((face1.astype("float") - face2.astype("float")) ** 2)
    return round(max(0, 100 - mse / 100), 2)

# ------------------ Upload Section ------------------
aadhar_image = st.file_uploader("📄 Upload Simulated Aadhar (Image)", type=["jpg", "jpeg", "png"])
selfie_image = st.file_uploader("🤳 Upload Selfie", type=["jpg", "jpeg", "png"])

if aadhar_image and selfie_image:
    st.markdown("---")
    st.image(aadhar_image, caption="📄 Aadhar Image", use_container_width=True)
    st.image(selfie_image, caption="🤳 Selfie Image", use_container_width=True)

    aadhar_pil = Image.open(aadhar_image)
    selfie_pil = Image.open(selfie_image)

    aadhar_cv = cv2.cvtColor(np.array(aadhar_pil), cv2.COLOR_RGB2BGR)
    selfie_cv = cv2.cvtColor(np.array(selfie_pil), cv2.COLOR_RGB2BGR)

    # ------------------ Processing ------------------
    dob_str = extract_dob_easyocr(aadhar_pil)
    age = calculate_age(dob_str)
    match = face_match(aadhar_cv, selfie_cv)

    st.write("📅 **Extracted DOB:**", dob_str)
    if age is not None:
        st.write("🎂 **Calculated Age:**", age)
    else:
        st.warning("⚠️ DOB format not recognized. Cannot calculate age.")

    st.metric("🧠 Face Match Score", f"{match}%")
    st.progress(min(100, int(match)))

    # ------------------ Final Decision ------------------
    if age is not None:
        if match > 70 and age >= 18:
            st.success("✅ Verified: Identity match and Age 18+")
        elif match <= 70:
            st.error("❌ Face does not match")
        elif age < 18:
            st.error("❌ User is under 18")
        else:
            st.warning("⚠️ Unexpected issue in verification")
    else:
        st.warning("⚠️ Cannot complete verification without valid DOB")
