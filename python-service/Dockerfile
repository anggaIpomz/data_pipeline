# Dockerfile for Python service
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the Python script
CMD ["python", "consume_and_insert.py"]
#CMD ["./wait-for-it.sh", "kafka:9092", "--", "python", "consume_and_insert.py"]
#CMD ["echo", "Hello, Darwin"]
