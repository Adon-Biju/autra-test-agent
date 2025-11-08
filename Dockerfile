FROM python:3.13-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY main.py .

# Set the handler
ENV HANDLER_MODULE=main
ENV HANDLER_FUNCTION=handler

# Run the agent
CMD ["python", "main.py"]
