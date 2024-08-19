import streamlit as st
import google.generativeai as geneai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")


# Configure the API key for the geneai model
geneai.configure(api_key=api_key)
model = geneai.GenerativeModel("gemini-pro")

def main():
    # Set the page configuration with a custom title and icon
    st.set_page_config(
        page_title="SQL Query Generator",
        page_icon=":robot:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Title and description
    st.title("SQL Query Generator")
    st.markdown(
        """
        **Welcome to the SQL Query Generator!**  
        This app allows you to generate SQL queries from natural language prompts.  
        Simply enter your prompt below and let the AI do the rest.
        """
    )

    # User input
    with st.form(key="query_form"):
        text_input = st.text_area(
            "Enter your query prompt here:",
            height=150,
            placeholder="e.g., Retrieve all customer names from the database where the purchase amount exceeds $1000"
        )
        
        submit_button = st.form_submit_button(label="Generate SQL Query")

    # Generate response if the submit button is pressed
    if submit_button:
        if text_input.strip() == "":
            st.warning("Please enter a query prompt before submitting.")
        else:
            with st.spinner("Generating SQL query..."):
                try:
                    response = model.generate_content(text_input)
                    st.success("SQL Query Generated Successfully!")
                    st.code(response.text, language="sql")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # Footer
    st.markdown(
        """
        ---
        **Powered by [GeneAI](https://example.com)**  
        _Crafted with :heart: using Streamlit by Ajeetkumar Ukande_
        """
    )

if __name__ == "__main__":
    main()


