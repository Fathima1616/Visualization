import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Scatter & Histogram App", layout="centered")

st.title("📊 Simple Visualization App")

# --- First radio button: data source ---
data_source = st.radio("Choose Data Source:", ["Manual input", "Random generated data"])

# --- Second radio button: visualization type ---
chart_type = st.radio("Choose Visualization:", ["Scatter plot", "Histogram"])

# Prepare dataframe based on choice
df = None

if data_source == "Manual input":
    st.subheader("Enter Data Manually")
    
    if chart_type == "Scatter plot":
        col1, col2 = st.columns(2)

        with col1:
            x_values = st.text_input("Enter X values (comma separated)", "1,2,3,4,5")
        with col2:
            y_values = st.text_input("Enter Y values (comma separated)", "2,4,6,8,10")

        try:
            x_list = [float(i.strip()) for i in x_values.split(",")]
            y_list = [float(i.strip()) for i in y_values.split(",")]
            if len(x_list) != len(y_list):
                st.error("❌ X and Y must have the same number of values.")
            else:
                df = pd.DataFrame({"X": x_list, "Y": y_list})
        except Exception:
            st.error("❌ Please enter valid numbers separated by commas.")

    elif chart_type == "Histogram":
        x_values = st.text_input("Enter X values (comma separated)", "1,2,3,4,5")
        try:
            x_list = [float(i.strip()) for i in x_values.split(",")]
            df = pd.DataFrame({"X": x_list})
        except Exception:
            st.error("❌ Please enter valid numbers separated by commas.")


elif data_source == "Random generated data":
    st.subheader("Random Data Generated")
    n = st.slider("Select number of data points:", 10, 200, 50, step=10)
    x = np.random.randn(n) * 10
    y = np.random.randn(n) * 5 + 20
    df = pd.DataFrame({"X": x, "Y": y})

# --- Visualization ---
if df is not None:
    if chart_type == "Scatter plot":
        st.subheader("Scatter Plot")
        fig = px.scatter(df, x="X", y="Y", title="Scatter Plot", color="Y")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Histogram":
        st.subheader("Histogram")
        fig = px.histogram(df, x="X", nbins=20, title="Histogram of X values")
        st.plotly_chart(fig, use_container_width=True)