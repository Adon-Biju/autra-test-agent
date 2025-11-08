FROM python:3.13-slim

# Create non-root user for security
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY main.py .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set the handler
ENV HANDLER_MODULE=main
ENV HANDLER_FUNCTION=handler

# Run the agent
CMD ["python", "main.py"]
