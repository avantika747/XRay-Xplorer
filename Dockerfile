# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /chestxray_project

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Installing Python dependencies
COPY requirements.txt /chestxray_project/
RUN pip install --no-cache-dir -r requirements.txt

# Copying the current directory contents into the container at /app
COPY . /chestxray_project/

# Running migrations
RUN python manage.py migrate