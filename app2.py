import streamlit as st
import google.generativeai as geneai
from dotenv import load_dotenv
import os
import sqlite3
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Retrive api key from the environment
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the api key for the geneai model
geneai.configure(api_key=api_key)
# model = geneai.GenerativeModel("Gemini-pro")
model = geneai.GenerativeModel("gemini-pro")

# Connect with PostgreSQL database
# def connect_db():
#     conn = psycopg2.connect(
#         dbname = "",
#         user="",
#         password="",
#         host=""
#     )
#     return conn



# # Connect to the SQLite database (or create it if it doesn't exist)
# def connect_db():
#     conn = sqlite3.connect("")
#     return conn

# Connect with MYSQL Database
import mysql.connector
def connect_db():
    conn = mysql.connector.connect(
        user='xxxx',
        password='xxxx',
        host='xxxx',
        database='xxx'
    )
    return conn

def execute_sql_query(query,conn):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return result
    except Exception as e:
        return str(e)
    
def main():
    # set the page configurations  with a custom title and icon
    st.set_page_config(
        page_title = "SQL Query Generator",
        page_icon = ":robot:",
        layout = "wide",
        initial_sidebar_state = "expanded",
    )

    # Title and Description
    st.title("SQL Query Generator")
    st.markdown(
        """
        **Welcome to the SQL Query Generator!**  
        This app allows you to generate SQL queries from natural language prompts and execute them on a database.  
        Simply enter your prompt below and let the AI do the rest.
        """
    )

    # user input
    with st.form(key='query_form') :
        text_input = st.text_area(
            "Enter your query Prompt here:",
            height = 150,
            placeholder = "e.g.,Retrival all customer names from the database where the purchase amount exceeds $1000"
        )
        submit_button = st.form_submit_button(label = "Generate and Execute SQL Query")
    
    # Generate response if the submit button is pressed
    if submit_button:
        if text_input.strip() == "":
            st.warming("Please enter the query prompt before submitting.")
        else:
            with st.spinner("Generating SQL query..."):
                try:
                    # Generate SQL Query from the prompt
                    response = model.generate_content(text_input)
                    st.success("SQL Query Generating Successfully!")
                    st.code(response.text,language="sql")

                    # Execute the SQL Query
                    conn = connect_db()
                    result = execute_sql_query(response.text,conn)
                    st.write("Query Result:")
                    st.write(result)

                    # close the datbase  connection
                    conn.close()
                except Exception as e:
                    st.error(f"An error occured:{e}")


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
