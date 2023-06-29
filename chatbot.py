import tkinter as tk
from tkinter import scrolledtext
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import csv
# Load the data from the CSV file
data_file = 'C:\\Users\\kumaran\\Desktop\\conversationo.csv'
questions = []
answers = []
with open(data_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        questions.append(row[0].lower())
        answers.append(row[1])
# Preprocess data
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)
preprocessed_questions = [preprocess_text(question) for question in questions]
# Training and testing data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)
# Build the model
similarity_matrix = cosine_similarity(X, X)
# Predict the response
def get_response(user_input):
    user_input = preprocess_text(user_input)
    user_vector = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_vector, X)
    best_match_index = np.argmax(similarity_scores)
    response = answers[best_match_index]
    return response
# GUI window
window = tk.Tk()
window.title("Cafe Chatbot")
window.geometry("400x500")
# Scrolled text widget for displaying the chat history
chat_history = scrolledtext.ScrolledText(window, width=50, height=20)
chat_history.pack(padx=10, pady=10)
# Entry widget for user input
user_input = tk.Entry(window, width=50)
user_input.pack(padx=10, pady=10)
# Function to handle user input and generate bot response
def process_input():
    query = user_input.get()
    user_input.delete(0, tk.END)
    if query.lower() == 'exit':
        window.quit()
    response = get_response(query)
    chat_history.insert(tk.END, "You: " + query + "\n")
    chat_history.insert(tk.END, "Bot: " + response + "\n")
    chat_history.insert(tk.END, "-" * 40 + "\n")
# Button to submit user input
submit_button = tk.Button(window, text="Send", command=process_input)
submit_button.pack(pady=10)
# Start the tkinter event loop
window.mainloop()