# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Ensure setup.sh is executable and run it
RUN chmod +x setup.sh && /bin/sh setup.sh

# Expose the Streamlit port
EXPOSE 8080

# Run Streamlit
CMD ["streamlit", "run", "Home_Demo.py", "--server.port=8080", "--server.address=0.0.0.0"]

