# SQL Query Generator-gemini-pro


Welcome to the **SQL Query Generator**! This application allows you to generate SQL queries from natural language prompts using AI.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [License](#license)
- [Author](#author)

## Features

- Generate SQL queries from plain English prompts.
- Easy-to-use interface powered by Streamlit.
- Secure API key management using environment variables.
- Real-time query generation with feedback for success or errors.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- `pip` for package management

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sql-query-generator.git
    cd sql-query-generator
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

4. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Start the application using the command above.
2. Open the provided URL (usually `http://localhost:8501`) in your web browser.
3. Enter a natural language prompt into the text area (e.g., "Retrieve all customer names from the database where the purchase amount exceeds $1000").
4. Click the "Generate SQL Query" button.
5. The generated SQL query will be displayed on the screen.

## Environment Variables

This application uses environment variables to securely manage API keys.

- `GOOGLE_API_KEY`: Your API key for the GeneAI service.

Make sure to store these values in a `.env` file in the root directory of your project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This application was crafted with :heart: using Streamlit by **Ajeetkumar Ukande**.

