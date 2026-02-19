# Use Python 3.12 slim base image
FROM python:3.12-slim

# Install system dependencies needed for opencv and pdf processing
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libxcb1 \
    libx11-6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Create static_pdfs directory if it doesn't exist
RUN mkdir -p static_pdfs

# Expose port (Railway uses PORT environment variable)
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
