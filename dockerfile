# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Playwright and browsers
RUN pip install playwright && playwright install --with-deps

# Copy all files from project into image
COPY . .

# Default command to run pytest with markers
#CMD ["pytest", "-m", "health_check", "--headed", "--maxfail=1", "--disable-warnings", "-v"]
