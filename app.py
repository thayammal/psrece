# To get user input and display it uing streamlit library
import streamlit as st


def main():
    # Set the title of the web app
    st.title("User Input and Display App")

    # Get user input using a text input box
    user_input = st.text_input("Enter Your Name")

    # Display the user input
    st.write(
        f'Hello, {user_input}! welcome to this first deployment of streamlit!')


if __name__ == "__main__":
    main()
