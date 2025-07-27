# Use the official Playwright image with Python and all dependencies
FROM mcr.microsoft.com/playwright/python:v1.51.0-focal

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code
COPY . .

# Optional: Default command
# CMD ["pytest", "-m", "health_check"]
