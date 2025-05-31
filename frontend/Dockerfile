# Use official Python base image
FROM python:3.10-slim

# # Set environment variables     // used while creating but while deploying on render.com, these are not needed.
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Create non-root user and app directory
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

# Set work directory
WORKDIR /app

# # Install system dependencies     // used while creating but while deploying on render.com, these are not needed.
# RUN apt-get update && apt-get install -y curl

# Install system dependencies (as root)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER appuser

# Copy and install Python dependencies
# COPY requirements.txt .
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
# COPY . .
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PATH="/home/appuser/.local/bin:${PATH}" \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Health check (for Render monitoring)
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Expose port
EXPOSE 8501

# # Run the application     // used while creating but while deploying on render.com, these are not needed.
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Production command
# CMD ["streamlit", "run", "app.py", \
#      "--server.port=8501", \
#      "--server.address=0.0.0.0", \
#      "--server.headless=true"]

CMD ["streamlit", "run", "app.py"]