# Product Catalog with Shopping Cart

A Django web application featuring a product catalog with category filtering and a session-based shopping cart system.

## Features

- Product catalog with categories
- Product filtering by category
- Session-based shopping cart (no user authentication required)
- Product image upload functionality
- Cart total calculations
- Responsive Bootstrap UI
- Admin interface for content management

## Quick Start

### Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Loickaltenbach/product-catalog.git
cd product-catalog
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Load sample data:**
```bash
python manage.py load_sample_data
```

6. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

8. **Run the development server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

### Docker Setup

1. **Using Docker Compose:**
```bash
docker-compose up --build
```

2. **Run migrations in container:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py load_sample_data
```

## Production Deployment

### Using the Deployment Script

1. **Run the deployment script:**
```bash
./deploy.sh
```

### Manual Production Setup

1. **Configure production settings:**
   - Copy `product_catalog/settings_production.py` settings
   - Set environment variables for database credentials
   - Configure `ALLOWED_HOSTS` with your domain

2. **Install production dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure database (PostgreSQL recommended):**
```bash
# Install PostgreSQL and create database
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres createdb product_catalog
```

4. **Run production commands:**
```bash
export DJANGO_SETTINGS_MODULE=product_catalog.settings_production
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser
```

5. **Configure web server (Nginx example):**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location /static/ {
        alias /var/www/static/;
    }
    
    location /media/ {
        alias /var/www/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Models

- **Category**: Product categories with name and description
- **Product**: Products with name, description, price, image, and category
- **Cart**: Session-based cart system (no database model required)

## API Endpoints

- `/` - Product list with category filtering
- `/product/<id>/` - Product detail view
- `/cart/` - Shopping cart view
- `/add-to-cart/<id>/` - Add product to cart
- `/update-cart/<id>/` - Update cart item quantity
- `/remove-from-cart/<id>/` - Remove item from cart
- `/clear-cart/` - Clear entire cart
- `/admin/` - Django admin interface

## Technologies Used

- **Backend**: Django 4.2, Python 3.10+
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Docker, Gunicorn, Nginx

## Project Structure

```
product_catalog/
├── catalog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── media/
│   └── products/
└── static/
```
