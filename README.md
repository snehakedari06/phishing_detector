
PHISHING_DETECTOR

An easy and effective Python tool to detect phishing URLs with rule-based heuristics and machine learning.

FEATURES:

Rule-Based Detection: Easily marks URLs with suspicious patterns (e.g., those containing @, %, or http://).

Machine Learning: Employs a Random Forest model trained on labeled URL datasets for sophisticated detection.

Graphical User Interface (GUI): Enables users to simply enter URLs and determine their safety status.

Scalable Design: Accommodates dynamic datasets for improved adaptability and precision.

PROJECT STRUCTURE:

phishing_detection_tool.py: Main script with the code for the tool.

url_dataset.csv: Dataset file (to be supplied) with labeled URLs.

README.md: Project documentation (this file).

REQUIREMENTS:

Python 3.8 or later

Libraries:

pandas

scikit-learn
tkinter

Install dependencies with:

bash

CopyEdit

pip install pandas scikit-learn

How to Use the Tool

Clone the repository onto your local machine:

bash

CopyEdit

git clone https://github.com/your-username/phishing-detection-tool.git cd phishing-detection-tool

Make sure the dataset file url_dataset.csv is in the project directory.

Run the script:

bash

CopyEdit

python phishing_detection_tool.py

Enter a URL in the GUI input field and click Check URL to view the outcome.

Dataset Format

The utility takes a CSV file (url_dataset.csv) as input with the following format:

URL: The URL to check.

Label: 1 for suspicious and 0 for safe URLs.

Example:

URLLabelhttp://example.com0https://phishing-site.org1

Screenshots

1. Input URL:

A straightforward input field to input the URL.

2. Result Display:

Displays whether the URL is safe or suspicious based on rule-based or machine learning detection.

Future Improvements

Utilize more complete datasets for increased accuracy.

Implement API integrations to provide real-time URL analysis.

Enhance rule-based validation to scan more phishing types.

Integrate a logging function to store results for analysis.

License

Licensed under the MIT License. Use, modify, and distribute freely.

Contributing

Contributions are encouraged! Fork the repository, implement your changes, and open a pull request.
