#!/bin/bash

# Deployment script for Product Catalog Django application

echo "Starting deployment..."

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Load sample data (only if needed)
echo "Loading sample data..."
python manage.py load_sample_data

echo "Deployment completed successfully!"
echo "Don't forget to:"
echo "1. Create a superuser: python manage.py createsuperuser"
echo "2. Configure your web server (nginx/apache)"
echo "3. Set up SSL certificates"
echo "4. Configure environment variables for production"
