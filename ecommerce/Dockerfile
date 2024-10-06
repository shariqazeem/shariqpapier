# Use the official Python image as base image
FROM python:3.10

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=ecommerce.settings
ENV DJANGO_DEBUG=False

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker cache for dependencies
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . /app

# Install Gunicorn
RUN pip install gunicorn

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose the port the app runs on
EXPOSE 8000

# Run the Django app with Gunicorn and better timeout/worker configuration
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecommerce.wsgi:application", "--workers", "3", "--timeout", "120"]
