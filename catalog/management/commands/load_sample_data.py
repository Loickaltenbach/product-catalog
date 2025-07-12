from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Load sample data for the product catalog'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
            {'name': 'Clothing', 'description': 'Fashion and apparel'},
            {'name': 'Books', 'description': 'Books and literature'},
            {'name': 'Home & Garden', 'description': 'Home and garden products'},
            {'name': 'Sports', 'description': 'Sports and fitness equipment'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create products
        products_data = [
            {
                'name': 'Smartphone Pro Max',
                'description': 'Latest flagship smartphone with advanced camera system and 5G connectivity. Features include a 6.7-inch Super Retina XDR display, A17 Pro chip, and professional camera system.',
                'price': Decimal('999.99'),
                'category': 'Electronics'
            },
            {
                'name': 'Wireless Headphones',
                'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life. Perfect for music lovers and professionals.',
                'price': Decimal('299.99'),
                'category': 'Electronics'
            },
            {
                'name': 'Classic T-Shirt',
                'description': 'Comfortable cotton t-shirt available in multiple colors. Made from 100% organic cotton for ultimate comfort.',
                'price': Decimal('24.99'),
                'category': 'Clothing'
            },
            {
                'name': 'Denim Jeans',
                'description': 'Classic fit denim jeans made from sustainable materials. Perfect for casual and semi-formal occasions.',
                'price': Decimal('79.99'),
                'category': 'Clothing'
            },
            {
                'name': 'Programming Fundamentals',
                'description': 'Complete guide to programming fundamentals covering multiple languages and best practices.',
                'price': Decimal('39.99'),
                'category': 'Books'
            },
            {
                'name': 'Science Fiction Novel',
                'description': 'Award-winning science fiction novel that explores the future of humanity and technology.',
                'price': Decimal('16.99'),
                'category': 'Books'
            },
            {
                'name': 'Coffee Maker',
                'description': 'Programmable coffee maker with built-in grinder and thermal carafe. Brew the perfect cup every time.',
                'price': Decimal('149.99'),
                'category': 'Home & Garden'
            },
            {
                'name': 'Garden Tool Set',
                'description': 'Complete 10-piece garden tool set with ergonomic handles and durable steel construction.',
                'price': Decimal('89.99'),
                'category': 'Home & Garden'
            },
            {
                'name': 'Yoga Mat',
                'description': 'Premium non-slip yoga mat made from eco-friendly materials. Perfect for yoga, pilates, and stretching.',
                'price': Decimal('49.99'),
                'category': 'Sports'
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight running shoes with advanced cushioning and breathable mesh upper. Designed for comfort and performance.',
                'price': Decimal('129.99'),
                'category': 'Sports'
            },
            {
                'name': 'Laptop Computer',
                'description': 'High-performance laptop with Intel i7 processor, 16GB RAM, and 512GB SSD. Perfect for work and gaming.',
                'price': Decimal('1299.99'),
                'category': 'Electronics'
            },
            {
                'name': 'Winter Jacket',
                'description': 'Waterproof winter jacket with down insulation. Keeps you warm and dry in harsh weather conditions.',
                'price': Decimal('199.99'),
                'category': 'Clothing'
            },
        ]
        
        for product_data in products_data:
            category = categories[product_data['category']]
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'category': category
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data!')
        )
