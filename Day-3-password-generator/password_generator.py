import streamlit as st  # Importing Streamlit for creating the web app
import random  # Importing random module to generate random choices
import string  # Importing string module to use predefined sets of characters

# Function to generate a password based on user preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Start with letters (both uppercase & lowercase)

    if use_digits:
        characters += string.digits  # Add numbers (0-9) if the user selects this option

    if use_special:
        characters += string.punctuation  # Add special characters (!, @, #, etc.) if selected

    # Generate a password by randomly selecting characters from the allowed set
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI title
st.title("Password Generator by Sadiq Khan")

# User input: Select password length using a slider (6 to 32 characters, default 12)
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# User input: Checkboxes to include digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Button to generate a password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # Call the function
    st.write(f"Generated Password: {password}")  # Display the generated password

st.write("------------------")  # Divider for UI separation

# Footer with credit and GitHub link
st.write("Built with ❤ by [Sadiq Khan](https://github.com/sadiqkhan7777)")
