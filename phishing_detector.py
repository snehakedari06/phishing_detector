import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from tkinter import Tk, Label, Entry, Button

def is_suspicious_url(url):
    """
    Simple rule-based check for suspicious URLs.
    """
    if "http://" in url or "@" in url or "%" in url:
        return True
    return False

def train_model():
    """
    Train a machine learning model using a URL dataset.
    """
    try:
        data = pd.read_csv("url_dataset.csv")
    except FileNotFoundError:
        print("Error: Dataset file 'url_dataset.csv' not found. Please add the file and try again.")
        exit()

    if data.empty:
        print("Error: Dataset is empty. Please provide a valid dataset.")
        exit()

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data["URL"])
    y = data["Label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model, vectorizer

def run_gui(model, vectorizer):
    """
    Launch a simple GUI to check URLs.
    """
    def check_url():
        url = url_entry.get().strip()
        if is_suspicious_url(url):
            result_label.config(text="Suspicious URL (Rule-Based Check)", fg="red")
        else:
            prediction = model.predict(vectorizer.transform([url]))
            if prediction[0] == 1:
                result_label.config(text="Suspicious URL (ML Check)", fg="red")
            else:
                result_label.config(text="Safe URL", fg="green")

    root = Tk()
    root.title("URL Safety Checker")

    Label(root, text="Enter a URL to check:").pack(pady=5)
    url_entry = Entry(root, width=50)
    url_entry.pack(pady=5)
    Button(root, text="Check URL", command=check_url).pack(pady=10)

    result_label = Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    print("Training the model... Please wait.")
    model, vectorizer = train_model()
    print("Model training complete. Launching the GUI tool...")
    run_gui(model, vectorizer)
