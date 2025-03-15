import streamlit as st
import requests

def get_random_joke():
    """Fetche a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why did the programmer quit his job? \n Because he didn't get arrays!"

def main():
    st.title("Random Joke Generator by Sadiq")
    st.write("Click the button below to generate a random joke:")

    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.write(joke)

        st.divider()
        
        st.markdown(
            """
            <div style='text-align: center;'>
            <p>Joke From Official Joke API</p>
            <p>Built with ❤️ by <a href="https://github.com/sadiqkhan7777">Sadiq Khan</a> Using streamlit</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        

if __name__ == "__main__":
    main()

