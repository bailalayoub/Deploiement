# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY . /app

# Install
RUN pip install -r requirement.txt

# Command to run on container start
CMD uvicorn main:app --port=8000 --host=0.0.0.0
