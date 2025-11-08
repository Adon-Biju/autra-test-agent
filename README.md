# Simple Text Processor Agent

A lightweight AI agent that processes and analyzes text using basic NLP techniques.

## Features
- Word count and character count
- Sentence detection
- Basic sentiment analysis
- Fast response time (< 1 second)

## Usage

```python
event = {
    'text': 'Your text here'
}

result = handler(event, context)
```

## Output Format

```json
{
    "status": "success",
    "word_count": 10,
    "character_count": 50,
    "sentence_count": 2,
    "sentiment": "positive",
    "sentiment_confidence": 0.3
}
```

## Requirements
- Python 3.13+
- No external dependencies

## License
MIT
