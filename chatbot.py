import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from difflib import SequenceMatcher
from dataset import training_data
from textblob import TextBlob

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# ==================== TEXT PREPROCESSING ====================
def preprocess_text(text):
    """
    Preprocess user query: convert to lowercase, tokenize, remove stopwords, and lemmatize
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    return processed_tokens

# ==================== INTENT RECOGNITION ====================
def calculate_similarity(str1, str2):
    """
    Calculate similarity between two strings using SequenceMatcher
    Returns a value between 0 and 1 (1 = identical, 0 = no match)
    """
    return SequenceMatcher(None, str1, str2).ratio()

def recognize_intent(user_query, training_data):
    """
    Find the best matching intent by comparing user query with training queries
    """
    processed_query = preprocess_text(user_query)
    query_string = ' '.join(processed_query)
    
    best_match = None
    best_similarity = 0
    
    for item in training_data:
        for query in item["queries"]:
            processed_training = preprocess_text(query)
            training_string = ' '.join(processed_training)
            
            similarity = calculate_similarity(query_string, training_string)
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = item
    
    return best_match, best_similarity

# ==================== NAMED ENTITY RECOGNITION ====================
def extract_entities(user_query):
    """
    Extract specific entities like order numbers from user query using regex
    """
    entities = {
        "order_id": None,
        "product_name": None
    }
    
    # Extract order number (pattern: #12345 or order 12345)
    order_match = re.search(r'#(\d+)|\border\s+(\d+)', user_query, re.IGNORECASE)
    if order_match:
        entities["order_id"] = order_match.group(1) or order_match.group(2)
    
    # Extract product name (simple version - can be enhanced)
    product_keywords = ["phone", "laptop", "tablet", "watch", "headphones"]
    for keyword in product_keywords:
        if keyword.lower() in user_query.lower():
            entities["product_name"] = keyword
            break
    
    return entities

# ==================== RESPONSE GENERATION ====================
def generate_response(user_query, training_data, context=None):
    """
    Generate response based on recognized intent and extracted entities
    Also analyzes sentiment for customer frustration detection
    Uses conversation context for multi-turn awareness
    """
    # Analyze sentiment
    sentiment = analyze_sentiment(user_query)
    
    # Recognize intent
    intent_data, similarity = recognize_intent(user_query, training_data)
    
    # If no good match found (low similarity), check if this is a follow-up
    if similarity < 0.3:
        # Check if user is asking a follow-up related to previous intent
        if context and context.get_last_intent():
            last_intent = context.get_last_intent()
            # Look for pronouns or context words indicating follow-up
            follow_up_indicators = ["it", "that", "this", "please", "still", "yet", "more"]
            if any(indicator in user_query.lower() for indicator in follow_up_indicators):
                # Use last intent as context
                intent_data = next((item for item in training_data if item["intent"] == last_intent), None)
                if intent_data:
                    similarity = 0.35  # Mark as contextual match
        
        if similarity < 0.3:
            return "I'm sorry, I didn't understand your question. Please try again."
    
    # Extract entities
    entities = extract_entities(user_query)
    
    # Get response template
    response = intent_data["response"]
    
    # Fill in entities if available
    if "{order_id}" in response and entities["order_id"]:
        response = response.format(order_id=entities["order_id"])
    
    # Add special handling for negative sentiment
    if sentiment["label"] == "negative":
        response = "I understand your frustration. " + response
    
    # Store in context
    if context:
        context.add_message("assistant", response, intent_data["intent"])
    
    return response

# ==================== SENTIMENT ANALYSIS ====================
def analyze_sentiment(user_query):
    """
    Analyze sentiment of user query to detect frustration
    Returns sentiment with label (positive, neutral, negative)
    """
    blob = TextBlob(user_query)
    polarity = blob.sentiment.polarity
    
    # Classify sentiment based on polarity score
    if polarity > 0.1:
        sentiment_label = "positive"
    elif polarity < -0.1:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"
    
    return {
        "polarity": polarity,
        "label": sentiment_label
    }

# ==================== CONVERSATION CONTEXT ====================
class ConversationContext:
    """
    Manages conversation history and context for multi-turn conversations
    """
    def __init__(self):
        self.conversation_history = []
    
    def add_message(self, role, content, intent=None):
        """
        Add a message to the conversation history
        role: 'user' or 'assistant'
        """
        self.conversation_history.append({
            "role": role,
            "content": content,
            "intent": intent
        })
    
    def get_last_intent(self):
        """
        Get the last recognized intent to provide context
        """
        for msg in reversed(self.conversation_history):
            if msg["intent"] and msg["role"] == "assistant":
                return msg["intent"]
        return None
    
    def get_conversation_summary(self, last_n=3):
        """
        Get summary of last N messages for context
        """
        recent = self.conversation_history[-last_n:]
        summary = []
        for msg in recent:
            summary.append(f"{msg['role']}: {msg['content']}")
        return "\n".join(summary)
    
    def clear_history(self):
        """
        Clear conversation history
        """
        self.conversation_history = []

# ==================== TEST THE CHATBOT ====================
print("\n" + "="*50)
print("CHATBOT RESPONSE TEST")
print("="*50)

test_queries = [
    "Where is my order #12345?",
    "How can I return a product?",
    "Does this phone support fast charging?"
]

for query in test_queries:
    response = generate_response(query, training_data)
    print(f"\nUser: {query}")
    print(f"Bot: {response}")

print("\n" + "="*50)
