FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

# Create a working directory for the application
WORKDIR /app

# Install any necessary system packages (if needed)
# RUN apt-get update && apt-get install -y some-package

# Copy requirements.txt into the container and install dependencies
COPY requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app will run on
EXPOSE 8080

# Start Gunicorn to serve the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "resume_app.wsgi:application"]