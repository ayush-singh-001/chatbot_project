# Training data - mapping intents to queries and responses
training_data = [
    {
        "intent": "order_status",
        "queries": [
            "Where is my order #12345?",
            "What is the status of order #12345?",
            "Track my order #12345",
            "When will order #12345 arrive?",
            "Has my order #99999 shipped yet?",
            "Can you check order #55555?",
            "I need to track order #77777",
            "Where's my package?",
            "When will it arrive?",
            "Status of my order?"
        ],
        "response": "Your order #{order_id} is out for delivery."
    },
    {
        "intent": "return_policy",
        "queries": [
            "How can I return a product?",
            "What is your return policy?",
            "Can I return items?",
            "How long do I have to return?",
            "What's the return deadline?",
            "Do you accept returns?",
            "How to return my order?",
            "Return window for products?",
            "Can I send it back?",
            "Refund policy information?"
        ],
        "response": "You can return products within 15 days via our online portal."
    },
    {
        "intent": "product_info",
        "queries": [
            "Does this phone support fast charging?",
            "What are the features?",
            "Does it have fast charging?",
            "Tell me about this product",
            "What's included in the box?",
            "Phone specifications?",
            "Does it support wireless charging?",
            "Battery life information?",
            "Camera quality details?",
            "Is fast charging available?"
        ],
        "response": "Yes, this phone supports fast charging."
    },
    {
        "intent": "shipping_time",
        "queries": [
            "How long for delivery?",
            "What's the shipping time?",
            "When will I receive it?",
            "Delivery timeframe?",
            "How many days to ship?",
            "Express shipping available?",
            "Estimated delivery date?",
            "Shipping options available?",
            "Can I get it faster?",
            "Rush delivery?"
        ],
        "response": "Standard delivery takes 5-7 business days. Express shipping is available for 2-day delivery."
    },
    {
        "intent": "payment_issue",
        "queries": [
            "Payment not working?",
            "Why was I charged twice?",
            "Card declined issue?",
            "Payment problem?",
            "Do you accept PayPal?",
            "What payment methods?",
            "Refund status?",
            "My payment failed",
            "Fix payment error?",
            "Why is payment stuck?"
        ],
        "response": "Please contact our support team at support@store.com for payment issues. They'll resolve it within 24 hours."
    }
]
