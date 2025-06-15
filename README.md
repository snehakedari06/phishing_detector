
Phishing Detection Tool
Ever wondered if a URL you’re about to click is safe? This tool helps you figure that out! It uses simple rules and a machine-learning model to check if a URL is safe or potentially dangerous.

What Does It Do?
Rule-Based Checks: Quickly flags suspicious URLs with patterns like %, @, or http://.

Machine Learning: Learns from a dataset to get smarter about detecting phishing.

Easy Interface: Just type in a URL and get an answer—safe or suspicious!

What You Need to Use This
Python 3.8 or higher.

A few Python libraries:

pandas

scikit-learn

tkinter (this one is built into Python).

To install the missing libraries, just run this in your terminal:

bash
Copy
Edit
pip install pandas scikit-learn
How to Use It
Download this project and open the folder.

Make sure you’ve got a file called url_dataset.csv in the same folder.

This file is like the brain of the tool—it teaches the model what’s safe and what’s not.

Open a terminal or command prompt in the project folder and run:

bash
Copy
Edit
python phishing_detection_tool.py
A window will pop up.

Type a URL into the box.

Hit the Check URL button.

Get your result: Safe or Suspicious.

What’s in the Dataset?
The dataset (url_dataset.csv) is pretty simple:

URL: The website link.

Label: 1 if it’s phishing, 0 if it’s safe.

Here’s an example of how it looks:

URL	Label
http://example.com	0
https://phishing-site.org	1

What Could Make This Better?
Adding more rules to catch tricky phishing URLs.

Using a bigger dataset to make it even smarter.

Keeping a history of checked URLs for reference.

