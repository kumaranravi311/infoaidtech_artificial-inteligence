# infoaidtech_artificial-inteligence
#Task 1
# Cafe Chatbot

The Café Chatbot is a simple conversational bot implemented using the `tkinter` library in Python. It uses a CSV file containing questions and answers to create a chatbot interface where users can interact with the bot.

## Prerequisites

Before running the Café Chatbot code, ensure that you have the following dependencies installed:

- Python (version 3.6 or higher)
- `tkinter`
- `numpy`
- `nltk`
- `scikit-learn`

You can install these dependencies using `pip`, the Python package installer.


## Usage

To use the Cafe Chatbot, follow these steps:

1. **Prepare the data**: Create a CSV file containing the conversation data. The file should have two columns: one for questions and one for corresponding answers. Each row represents a question-answer pair. Make sure the CSV file path is correctly set in the `data_file` variable.

2. **Run the code**: Execute the Python script that contains the Café Chatbot code. This will launch a GUI window with a chat interface.

3. **Chat with the bot**: Type your questions in the input field and press Enter or click the "Send" button to submit your query. The bot will process your input and provide a response based on the preloaded data.

4. **Exit the chat**: To exit the chat, type "exit" (case insensitive) in the input field and press Enter or click the "Send" button.

## How it works

The Café Chatbot uses the following steps to generate responses:

1. **Data loading**: It reads the questions and answers from a CSV file and stores them in separate lists.

2. **Data preprocessing**: The questions are preprocessed using tokenization and lemmatization techniques provided by the NLTK library. This step ensures that the input and stored questions are in a consistent format.

3. **Model training**: The preprocessed questions are transformed into numerical vectors using the TF-IDF vectorization technique provided by the scikit-learn library. These vectors are then used to calculate the cosine similarity matrix.

4. **Response generation**: When a user input is received, it is preprocessed in the same way as the training data. The preprocessed input is then transformed into a vector and compared with the vectors of the stored questions using cosine similarity. The question with the highest similarity score is considered the best match, and its corresponding answer is retrieved as the response.

5. **User interface**: The bot's responses and the user's input are displayed in a scrolled text widget within a tkinter window. The user can continue the conversation by entering new queries in the input field and receiving responses from the bot.
