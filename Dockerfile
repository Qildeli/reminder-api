# official Python runtime as a parent image
FROM python:3.10.12

# Environment variables
ENV PYTHONUNBUFFERED 1

# Working directiory
WORKDIR /app

# Add the current directory files to the container
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt # or pip install --no-cache-dir -r requirements.txt

# Expose the port server is running on
Expose 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]