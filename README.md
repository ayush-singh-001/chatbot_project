# Customer Support Chatbot

## Overview
An intelligent chatbot system designed to handle basic customer queries for online shopping platforms. The chatbot uses Natural Language Processing (NLP) to understand customer intent and provide appropriate responses.

## Features Implemented

### Core Features
1. **Intent Recognition** - Classifies user queries into predefined categories:
   - Order Status
   - Return Policy
   - Product Information
   - Shipping Time
   - Payment Issues

2. **Named Entity Recognition (NER)** - Extracts specific information:
   - Order numbers (e.g., #12345)
   - Product names
   - Entities are dynamically inserted into responses

3. **Text Preprocessing** - Enhances query understanding:
   - Tokenization
   - Stopword removal
   - Lemmatization
   - Special character removal

4. **Sentiment Analysis** - Detects customer emotion:
   - Identifies positive, negative, and neutral sentiment
   - Provides empathetic responses to frustrated customers
   - Shows sentiment scores in the UI

### User Interface
- Web-based interface built with Streamlit
- Real-time chat interaction
- Chat history preservation
- Visual sentiment indicators with emojis

## Project Structure

```
chatbot_project/
├── chatbot.py          # Main chatbot logic
├── dataset.py          # Training data and intents
├── app.py              # Streamlit web interface
├── README.md           # This file
└── venv/               # Virtual environment
```

## Files Description

### chatbot.py
Contains all NLP functions:
- `preprocess_text()` - Text preprocessing
- `recognize_intent()` - Intent classification
- `extract_entities()` - Named entity recognition
- `generate_response()` - Response generation
- `analyze_sentiment()` - Sentiment analysis

### dataset.py
Defines training data with 5 intent categories and 50+ training examples

### app.py
Streamlit application providing:
- Chat interface
- Sentiment visualization
- Message history

## Technologies Used

- **Python 3.10**
- **NLTK** - Natural Language Toolkit for NLP
- **spaCy** - Advanced NLP library
- **TextBlob** - Sentiment analysis
- **Streamlit** - Web interface framework

## How to Run

1. **Activate virtual environment:**
   ```
   venv\Scripts\activate
   ```

2. **Run CLI version:**
   ```
   python chatbot.py
   ```

3. **Run web interface:**
   ```
   streamlit run app.py
   ```

## Example Queries

| Intent | Example Query | Expected Response |
|--------|---------------|-------------------|
| Order Status | "Where is my order #12345?" | "Your order #12345 is out for delivery." |
| Return Policy | "How long do I have to return?" | "You can return products within 15 days via our online portal." |
| Product Info | "Does this phone support fast charging?" | "Yes, this phone supports fast charging." |
| Shipping Time | "How long for delivery?" | "Standard delivery takes 5-7 business days..." |
| Payment Issue | "Why was I charged twice?" | "Please contact our support team..." |

## Future Enhancements

1. **Machine Learning Integration** - Replace rule-based matching with ML classifiers (Naive Bayes, SVM)
2. **Database Integration** - Connect to live order database for real-time information
3. **Multi-language Support** - Support queries in multiple languages
4. **Context Awareness** - Remember conversation context for follow-up questions
5. **Advanced NER** - Use spaCy models for better entity extraction

## How It Works

1. User enters a query
2. System preprocesses the text (tokenize, remove stopwords, lemmatize)
3. Intent is recognized using string similarity matching
4. Named entities are extracted using regex patterns
5. Sentiment is analyzed using TextBlob polarity scores
6. Response template is selected based on intent
7. Entities are inserted into the response template
8. Special handling for negative sentiment adds empathy

## Limitations & Future Work

- Currently uses rule-based and similarity matching (not ML)
- Limited to predefined intents (extensible in dataset.py)
- Order numbers must be in format #XXXXX
- No persistent storage of conversations
- No integration with actual order database

## Author
Created as part of Customer Support Chatbot assignment

## License
MIT License
