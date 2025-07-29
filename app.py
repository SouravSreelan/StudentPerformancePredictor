import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

model = pickle.load(open("model/model.pkl", "rb"))

st.set_page_config(page_title="🎓 Student Performance Predictor", layout="centered")
st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final exam score (G3) based on academic and lifestyle features.")

df = pd.read_csv("data/student-mat.csv", sep=';' )
features = ['studytime', 'failures', 'absences', 'G1', 'G2', 'age', 'Medu', 'Fedu', 'goout', 'Dalc', 'Walc']
df = df[features + ['G3']]

st.sidebar.header("📋 Student Inputs")

def user_inputs():
    studytime = st.sidebar.slider("📚 Study Time (1–4)", 1, 4, 2)
    failures = st.sidebar.selectbox("❌ Past Failures", [0, 1, 2, 3])
    absences = st.sidebar.slider("📉 Absences", 0, 100, 4)
    G1 = st.sidebar.slider("📝 Grade 1 (G1)", 0, 20, 10)
    G2 = st.sidebar.slider("📝 Grade 2 (G2)", 0, 20, 10)
    age = st.sidebar.slider("🎂 Age", 15, 22, 17)
    Medu = st.sidebar.slider("👩‍🎓 Mother's Education (0–4)", 0, 4, 2)
    Fedu = st.sidebar.slider("👨‍🎓 Father's Education (0–4)", 0, 4, 2)
    goout = st.sidebar.slider("🎉 Social Life (1–5)", 1, 5, 3)
    Dalc = st.sidebar.slider("🍺 Daily Alcohol (1–5)", 1, 5, 1)
    Walc = st.sidebar.slider("🍷 Weekend Alcohol (1–5)", 1, 5, 2)

    input_df = pd.DataFrame([[studytime, failures, absences, G1, G2, age, Medu, Fedu, goout, Dalc, Walc]],columns=features)
    return input_df

input_df = user_inputs()

if st.sidebar.button("🎯 Predict Final Grade"):
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(20, prediction))  
    st.success(f"🎓 Predicted Final Grade: **{prediction:.2f} / 20**")

st.subheader("📊 Data Visualizations")
st.markdown("🔍 Correlation Heatmap")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax1)
st.pyplot(fig1)

st.markdown("## Grade Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df["G3"], bins=20, kde=True, ax=ax2, color="skyblue")
st.pyplot(fig2)

st.markdown("### Feature Importance (Top Predictors)")
importances = model.feature_importances_
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

fig3, ax3 = plt.subplots()
sns.barplot(x='Importance', y='Feature', data=importance_df, ax=ax3)
st.pyplot(fig3)

