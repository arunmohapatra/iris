# Use Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY src/app.py models/model.pkl requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
