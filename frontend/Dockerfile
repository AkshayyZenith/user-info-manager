# Use official Python base image
FROM python:3.10-slim

# # Set environment variables     // used while creating but while deploying on render.com, these are not needed.
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# # Install system dependencies     // used while creating but while deploying on render.com, these are not needed.
# RUN apt-get update && apt-get install -y curl

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# # Run the application     // used while creating but while deploying on render.com, these are not needed.
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Production command
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true"]