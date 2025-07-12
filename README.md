# Product Catalog with Shopping Cart

A Django web application featuring a product catalog with category filtering and a session-based shopping cart system.

## Features

- Product catalog with categories
- Product filtering by category
- Session-based shopping cart (no user authentication required)
- Product image upload functionality
- Cart total calculations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

## Models

- **Category**: Product categories
- **Product**: Products with name, description, price, and image
- **Cart**: Session-based cart system (no database model)

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
