# 🎓 Student Performance Predictor

A simple machine learning web app to predict a student's final exam score based on study time, past grades, and attendance. Built with Python, scikit-learn, and deployed using Streamlit.

## 🚀 Live Demo
👉 [View Demo on Streamlit Cloud](https://studentperformancepredictor-j3jdrnrgzdtuyagsdipv7f.streamlit.app/)

---

## 📦 Features

- Predict final exam score (`G3`)
- Visualize student performance and correlations
- Interactive sliders for inputs
- Clean and modern UI built with Streamlit

---

## 📊 Sample Inputs

| Feature     | Description                          |
|-------------|--------------------------------------|
| studytime   | Weekly study hours (1 = low, 4 = high) |
| failures    | Number of past class failures        |
| absences    | Number of school absences            |
| G1          | First period grade (0–20)            |
| G2          | Second period grade (0–20)           |

---

## 🧠 Model Details

- **Model**: Linear Regression
- **Training Set**: UCI Student Performance Dataset (`student-mat.csv`)
- **Target**: Final Grade (G3)

---

## ⚙️ How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor
```
Install dependencies:
  pip install -r requirements.txt
  
Run the app:
  streamlit run app.py

