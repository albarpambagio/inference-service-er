# Use the official Python image from Docker Hub as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy just the requirements file
COPY requirements.txt .

# Install dependencies only if requirements.txt has changed
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose ports if needed
EXPOSE 8000 

# Command to run FastAPI and Streamlit concurrently
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000""]
