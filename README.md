
## 📄 `README.md` — FaceIQ

# 📷 FaceIQ

**FaceIQ** is a lightweight, AI-powered application designed for **age and identity verification**. It uses Optical Character Recognition (OCR) to extract Date of Birth (DOB) from a simulated Aadhar card and compares it with a live selfie using face detection. Built for the **Zynga Hackathon 2025**, this app helps simulate real-world use cases like verifying users for age-restricted platforms or government services.

---

## 🚀 Features

- 📄 Uploads simulated Aadhar card and selfie
- 🔍 Extracts DOB using EasyOCR (no external Tesseract setup)
- 🎂 Calculates age from extracted DOB
- 🧠 Matches faces using OpenCV Haar Cascade
- ✅ Confirms if user is 18+ and if face matches
- 💻 Built with Streamlit — simple, fast, interactive

---

## 🧠 How It Works

1. **User uploads** a simulated Aadhar card and a selfie.
2. **OCR engine** reads DOB from the document.
3. **Face detection** extracts face regions from both images.
4. **Matching algorithm** compares faces and shows confidence score.
5. **Decision logic** validates age and face match to verify identity.

---

## 🖥 Tech Stack

| Component        | Technology               |
|------------------|---------------------------|
| Web UI           | Streamlit                |
| OCR Engine       | EasyOCR (PyTorch-based)  |
| Image Processing | OpenCV                   |
| Face Detection   | Haar Cascade XML         |
| Language         | Python 3.x               |

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/faceiq.git
cd faceiq
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run faceiq_app.py
```

---

## 📝 Requirements

```txt
streamlit
easyocr
opencv-python-headless
numpy
pillow
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this code to a GitHub repo
2. Visit [https://share.streamlit.io](https://share.streamlit.io)
3. Select your repo and `faceiq_app.py` as the main file
4. Click **Deploy**

---

## 📷 Sample Use Case

> “Verify if a person is eligible to register for an online service (e.g., alcohol delivery, legal contracts, etc.) by checking whether their face matches the uploaded ID and they are at least 18 years old.”

---

## 🔒 Disclaimer

This is a **prototype/demo** built for educational and hackathon purposes. It does not process real Aadhaar cards and is not meant for production identity verification.

---




## ⭐️ Show some ❤️

If you like this project, don't forget to ⭐ the repo!

