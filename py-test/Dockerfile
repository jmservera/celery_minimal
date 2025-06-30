FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY main.py .

# Make the script executable
RUN chmod +x main.py

# Run the application
CMD ["sh","-c","python3 main.py"]
