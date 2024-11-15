import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("Basic Streamlit Web App")

# Sidebar
st.sidebar.header("Navigation")
options = st.sidebar.selectbox("Select a page:", ["Home", "Data Input", "Visualization"])

# Home Page
if options == "Home":
    st.header("Welcome to My Practice App!")
    st.write("This is a basic Streamlit app for deployment practice.")
    st.write("Explore the options in the sidebar to see what this app can do!")

# Data Input Page
elif options == "Data Input":
    st.header("Input Data")
    name = st.text_input("What's your name?")
    age = st.number_input("How old are you?", min_value=0, max_value=120, value=25, step=1)

    if st.button("Submit"):
        st.write(f"Hello, {name}! You are {age} years old.")

# Visualization Page
elif options == "Visualization":
    st.header("Simple Visualization")

    # Generate sample data
    data = {
        "Category": ["A", "B", "C", "D"],
        "Values": [10, 23, 7, 15]
    }
    df = pd.DataFrame(data)

    # Display data
    st.write("Here is some sample data:")
    st.dataframe(df)

    # Bar chart
    st.write("Bar chart of the data:")
    plt.bar(df["Category"], df["Values"])
    st.pyplot(plt)
