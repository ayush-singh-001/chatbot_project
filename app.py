import streamlit as st
from chatbot import generate_response, analyze_sentiment, ConversationContext
from dataset import training_data

# Page configuration
st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

# Title and description
st.title("🤖 Customer Support Chatbot")
st.markdown("Ask me about orders, returns, or product information!")

# Initialize conversation context in session state
if "context" not in st.session_state:
    st.session_state.context = ConversationContext()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a clear button in sidebar
with st.sidebar:
    st.markdown("### Options")
    if st.button("🔄 Clear Conversation"):
        st.session_state.context.clear_history()
        st.session_state.messages = []
        st.success("Conversation cleared!")
    
    # Show conversation summary
    if st.session_state.messages:
        st.markdown("### Conversation Summary")
        st.markdown(f"**Total messages:** {len(st.session_state.messages)}")
        
        # Show last intent if available
        last_intent = st.session_state.context.get_last_intent()
        if last_intent:
            st.markdown(f"**Last topic:** {last_intent.replace('_', ' ').title()}")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sentiment" in message:
            sentiment = message["sentiment"]
            if sentiment["label"] == "negative":
                st.warning(f"😞 Negative sentiment detected (score: {sentiment['polarity']:.2f})")
            elif sentiment["label"] == "positive":
                st.success(f"😊 Positive sentiment detected (score: {sentiment['polarity']:.2f})")

# User input
if prompt := st.chat_input("Type your question here..."):
    # Analyze sentiment
    sentiment = analyze_sentiment(prompt)
    
    # Add user message to Streamlit chat history
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt,
        "sentiment": sentiment
    })
    
    # Add user message to context
    st.session_state.context.add_message("user", prompt)
    
    # Display user message with sentiment
    with st.chat_message("user"):
        st.markdown(prompt)
        if sentiment["label"] == "negative":
            st.warning(f"😞 Negative sentiment detected (score: {sentiment['polarity']:.2f})")
        elif sentiment["label"] == "positive":
            st.success(f"😊 Positive sentiment detected (score: {sentiment['polarity']:.2f})")
    
    # Generate bot response with context
    response = generate_response(prompt, training_data, st.session_state.context)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
