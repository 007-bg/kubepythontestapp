# Use a lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies (none required but keep step for future additions)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py /app/

# Expose default port
EXPOSE 8000

# Default environment for container
ENV PORT=8000
ENV HOST=0.0.0.0

# Run the app
CMD ["python", "app.py"]
