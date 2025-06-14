# Use official Python base image
FROM python:3.9-slim

# # Set environment variables     // used while creating but while deploying on render.com, these are not needed.
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Create non-root user
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

# Set work directory
WORKDIR /app

# # Install system dependencies     // used while creating but while deploying on render.com, these are not needed.
# RUN apt-get update && apt-get install -y gcc

# Install as root (system deps)
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER appuser

# Copy and install Python dependencies  
# first (for layer caching)
# COPY requirements.txt .
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
# COPY . .
COPY --chown=appuser:appuser . .

# Ensure Python can find user-installed packages
ENV PATH="/home/appuser/.local/bin:${PATH}"

# # Expose port     // used while creating but while deploying on render.com, these are not needed.
# EXPOSE 8000

# # Run the application     // used while creating but while deploying on render.com, these are not needed.
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Production command (no --reload)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]