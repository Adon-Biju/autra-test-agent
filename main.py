"""
Simple Text Processor Agent
A lightweight agent that processes text and returns basic analytics
"""

def handler(event, context):
    """
    Main handler function for the agent
    
    Args:
        event: Input data containing 'text' field
        context: Execution context
        
    Returns:
        dict: Processed results
    """
    # Get input text
    text = event.get('text', '')
    
    if not text:
        return {
            'error': 'No text provided',
            'status': 'failed'
        }
    
    # Basic text processing
    word_count = len(text.split())
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Simple sentiment analysis (basic keyword matching)
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'poor', 'disappointing']
    
    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        sentiment = 'positive'
    elif negative_count > positive_count:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    # Return results
    return {
        'status': 'success',
        'word_count': word_count,
        'character_count': char_count,
        'sentence_count': sentence_count,
        'sentiment': sentiment,
        'sentiment_confidence': max(positive_count, negative_count) / max(word_count, 1)
    }


# For local testing
if __name__ == '__main__':
    # Test the handler
    test_event = {
        'text': 'This is a great and wonderful test. The results are amazing!'
    }
    
    result = handler(test_event, None)
    print('Test Result:', result)
