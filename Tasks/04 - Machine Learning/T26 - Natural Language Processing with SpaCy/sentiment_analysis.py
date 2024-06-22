# Practical Task 1

# Import libraries
import numpy as np
import pandas as pd
import re
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Import Reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 1. Implement a sentiment analysis model using spaCy
# Load spacy model
nlp = spacy.load("en_core_web_sm")

# Add spacytextblob to the processing pipeline
nlp.add_pipe("spacytextblob")

# 2. Preprocess the text data
# Load the dataset
reviews_df = pd.read_csv("amazon_product_reviews.csv")

# Select the 'review.text' column
reviews_data = reviews_df["reviews.text"]
print("Review data head:\n", reviews_data.head())
print("Review data shape: ", reviews_data.shape)

# Remove all missing values
# Show the null sum
print("Rview data null sum, ", reviews_data.isnull().sum())

# Only 1 null, so simply drop it
reviews_data.dropna(inplace=True)
print("Rview data null sum check, ", reviews_data.isnull().sum())

# Preprocess on single review 
def preprocess_review_text(review):
    # Lower case
    review = review.lower()

    # Remove spaces at the beginning and at the end of the review
    review = review.strip()

    # Remove special characters
    review = re.sub("[^A-Za-z]+", " ", review) 

    # Tokenise and Remove integers, stopwords, punctuations, currency and spaces
    doc = nlp(review)
    takes = []
    for taken in doc:
        if taken.is_punct or taken.is_stop or taken.is_digit or not(taken.is_oov) or taken.is_currency or taken.is_space or (len(taken.text) <= 2):
            pass
        else:
            # Lemmatization
            takes.append(taken.lemma_.lower())
    return " ".join(takes)

text = "This product so far has not disappointed. My children love to use it and I like the ability to monitor control what content they see with ease."
print(preprocess_review_text(text))

# Preprocess top 50 data of all reviews, because all 34660 reviews to preprocessed so long time.
reviews_data_preprocessed = reviews_data.head(50).apply(preprocess_review_text)
print("Review data preprocessed head:\n", reviews_data_preprocessed.head())

# 3. Create a function for sentiment analysis
def analyze_sentiment(review):
    doc = nlp(review)
    polarity = doc._.blob.polarity
    if polarity > 0.25:
        sentiment = "Positive"
    elif polarity < -0.25:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

# 4. Test the model on sample product reviews
# Analyse the reviews sentiment
sample_reviews = reviews_data_preprocessed.head()
for review in sample_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}\nSentiment: {sentiment}\n")

# Compare the similarity of two product reviews
# As similarity method, we use use largeer model en_core_web_md
nlp_md = spacy.load("en_core_web_md")
for review1 in sample_reviews:
    doc1 = nlp_md(review1)
    for review2 in sample_reviews:
        doc2 = nlp_md(review2)
        if review1 != review2:
            similarity = doc1.similarity(doc2)
            print(f"Review1: {review1}\nReview2: {review2}\nSimilarity: {similarity}\n")

# 5. Write a brief report or summary in a PDF file - sentiment_analysis_report.pdf
report = """
# Sentiment Analysis Report

## Description of the Dataset
- The data is a list of over 34,000 consumer reviews for Amazon products. 
- We focus on the 'reviews.text' column, which contains the product reviews.

## Preprocessing Steps
1. Load spacy model
2. Load the dataset
3. Clean data
    * Remove all missing values
    * Lower case 
4. Preprocess the text
    * Tokenise
    * Remove special characters
    * Remove integers, stopwords, punctuations, currency and spaces
    * Lemmatization

## Evaluation of Results
### Sentiment Analysis Results
- We test on sample reviews. Polarity scores range from -1 (very negative) to 1 (very positive).
- All the sample reviews are positive sentiment. The products are well-received by customers.

### Similarity Analysis
- Each two reviews were compared for similarity. 
- The higher similarity scores are, the more similar the two reviews are.

## Model Strengths and Limitations
### Strengths:
- SpaCy and TextBlob are powerful tools for text processing and sentiment analysis.
- Text preprocessing to clean the data is so effective.
### Limitations:
- The sentiment analysis is relatively simple and might not capture complex nuances in sentiment.
"""

# pdf file path
file_path = "sentiment_analysis_report.pdf"

# Create a canvas object
canvas_pdf = canvas.Canvas(file_path, pagesize=A4)

# Split the report into lines to fit into the PDF
lines = report.splitlines()

# Set initial y coordinate for writing text
y = A4[1] - 30

# Write each line to the PDF
for line in lines:
    canvas_pdf.drawString(30, y, line)
    y -= 15  # Move y coordinate down for the next line

# Save the PDF file
canvas_pdf.save()



