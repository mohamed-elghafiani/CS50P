# Intro to CS Course - Lectures Code Resourses

# For the chatbot part

## Installation

To get started, follow these steps:

1. **Download the Repository**

   - Click the "Code" button at the top of this page.
   - Select "Download ZIP" to download the repository as a `.zip` file.
   - Extract the contents of the downloaded file to a directory of your choice.

2. **Navigate to the Chatbot Directory**

   - Open your terminal or command prompt.
   - Use the `cd` command to navigate into the `chatbot` directory within the extracted repository:

     ```bash
     cd chatbot
     ```

3. **Create a Virtual Environment (Optional but Recommended)**

   - It's a good practice to create a virtual environment to manage your project's dependencies. To create a virtual environment, run:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
   
     - On Windows:

       ```bash
       Set-ExecutionPolicy bypass -scope process
       venv\Scripts\activate
       ```

     - On macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**

   - Install the project's dependencies using `pip` with the provided `requirements.txt` file:

     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Chatbot**

   - You're now ready to run the chatbot! Execute the following command to start the chatbot:

     ```bash
     python bot.py
     ```

   The chatbot should now be up and running, and you can start interacting with it.
