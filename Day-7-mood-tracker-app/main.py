import streamlit as st # For creating web interface
import pandas as pd # for data manipulation
import datetime # for handling dates
import csv  # for reading and writing csv files
import os   # for file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# function to read mood data from a CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # if no files, create empty Dataframe and column
        return pd.DataFrame(columns=["Date", "Mood"])
    # Read and Return existing mood data
    return pd.read_csv(MOOD_FILE)

# function to add new mood entry to the CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:

        # Create CSV writer
        writer = csv.writer(file)
        
        # 
        writer.writerow([date, mood])

st.title("Mood Tracker by Sadiq")

today = datetime.date.today()

st.subheader("How are your feeling today?")

mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Neutral", "Angry"])

if st.button("Log Mood"):

    save_mood_data(today, mood)

    st.success("Mood Logged Successfully!")

data = load_mood_data() 

if not data.empty:

    st.subheader("Mood Trends Over Time")
    
    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

# Build with love by Sadiq khan
st.write("Build with ❤ by [Sadiq khan](https://github.com/sadiqkhan7777)")
