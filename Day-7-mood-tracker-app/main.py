import streamlit as st # For creating web interface
import pandas as pd # For data manipulation
import datetime # For handling dates
import csv # For reading and writing CSV file
import os # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

Function to read mood data from the CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    
    try:
        return pd.read_csv(MOOD_FILE, on_bad_lines="skip")  # Corrected version
    except pd.errors.ParserError:
        st.error("Error reading CSV file! Please check its format.")
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:

        # Create CSV writer
        writer = csv.writer(file)

        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are your feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    
    # Save mood when button is clicked
    save_mood_data(today, mood)

    # Show success message
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:

    # Create section for Visualization
    st.subheader("Mood Trends Over Time")

    # Convert date stings to datetime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)
# Build with love by Sadiq Khan
    st.write("Build with ❤️ by [Sadiq Khan](https://github.com/sadiqkhan7777/ramadan-coding-nights)")

    
