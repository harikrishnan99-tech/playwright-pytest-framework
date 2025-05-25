# Use official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    git \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm-dev \
    libxshmfence-dev \
    libasound2 \
    libx11-xcb1 \
    libxss1 \
    libgtk-3-0 \
    libglu1-mesa \
    fonts-liberation \
    libappindicator3-1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright and browsers
RUN pip install playwright && playwright install --with-deps

# Copy all files from project into image
COPY . .

# Default command to run pytest with markers
CMD ["pytest", "-m", "health_check", "--headed", "--maxfail=1", "--disable-warnings", "-v"]
