FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy only the necessary files
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gunicorn will run on
EXPOSE 5000

# Command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fizzbuzz_server.wsgi:app"]