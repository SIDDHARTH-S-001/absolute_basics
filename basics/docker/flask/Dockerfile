# Base image with python.
FROM python:3.10

# Set working directory.
WORKDIR /app

# Install dpeendencies.
COPY requirements.txt . 
RUN pip install -r requirements.txt

# Copy source code.
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the app.
CMD ["python", "app.py"]