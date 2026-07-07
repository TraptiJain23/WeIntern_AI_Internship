# 🌿 AgriShield AI – Plant Disease Classifier

An AI-powered web application that detects plant leaf diseases from uploaded images or live camera capture using a deep learning model. The application predicts the disease, displays the confidence score, and provides treatment recommendations to help farmers and gardeners take timely action.

---

## 🚀 Live Demo

🔗 **Hugging Face Space:**  
[https://YOUR_HF_LINK](https://huggingface.co/spaces/jaintapti/AgriShield-AI-Plant-Disease-Classifier)

---

##  Features

-  Detects diseases from plant leaf images
-  Supports both image upload and camera capture
-  Deep Learning-based disease prediction
-  Displays prediction confidence
-  Provides disease remedies and treatment suggestions
-  Responsive and user-friendly interface

---

## AI Model

- **Framework:** TensorFlow / Keras
- **Model Type:** CNN-based Image Classification (MobileNetV2 Transfer Learning)
- **Dataset:** PlantVillage Dataset
- **Number of Classes:** 38
- **Input Image Size:** 224 × 224 pixels

---

##  Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask (Python)

### AI & Machine Learning
- TensorFlow
- Keras
- NumPy
- OpenCV
- Pillow

### Deployment
- Hugging Face Spaces (Docker)

---

## 📂 Project Structure

```text
plant-disease-detection-project/
│
├── app.py
├── remedies.py
├── plant_disease_model.h5
├── class_indices.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── static/
├── templates/
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/TraptiJain23/plant-disease-detection-project.git
```

Move into the project directory

```bash
cd AgriShield-AI-Plant-Disease-Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open in your browser

```
http://127.0.0.1:7860
```

---

##  How It Works

1. Upload a plant leaf image or capture one using your camera.
2. The image is preprocessed.
3. The trained TensorFlow model predicts the disease.
4. The application displays:
   - Predicted Disease
   - Confidence Score
   - Recommended Remedy

---

## 🌾 Dataset

- **Dataset:** PlantVillage Dataset(Source-Kaggle)
- **Classes:** 38
- **Image Size:** 224 × 224
- **Preprocessing:**
  - RGB Conversion
  - Image Resizing
  - MobileNetV2 Preprocessing

---

##  Deployment

This project is deployed using **Hugging Face Spaces (Docker)**.

Live Application:

🔗 [https://YOUR_HF_LINK](https://huggingface.co/spaces/jaintapti/AgriShield-AI-Plant-Disease-Classifier)

---

## Author

**Trapti Jain**


---

##  License

This project is created as minor team project under AI internship at WeIntern. 
### Team members-
Nunna Harish Chandra Surya Bhaskar
Ishita Bhadoriya
Vratika Kumawat
Arya Kothari 
Trapti Jain






