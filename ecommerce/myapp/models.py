from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos')

    def __str__(self):
        return self.name
    
class Caraousel(models.Model):
    image = models.ImageField(upload_to='carousel_images')
    brand_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.brand_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/')
    sold_out = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    main_product = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1) # Set default category

    def __str__(self):
        return self.title


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('paypro', 'PayPro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='')  
    email = models.EmailField(default='')  
    country = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    postal_code = models.CharField(max_length=20, default='')
    phone_number = models.CharField(max_length=20, default='')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Total bill for the order

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in order {self.order.id}"


class CustomerRate(models.Model):
    customer_name = models.CharField(max_length=255)
    paper_width = models.FloatField()
    paper_height = models.FloatField()
    gram = models.FloatField()
    gram_rate = models.FloatField()
    sheet = models.FloatField()
    labour_cost = models.FloatField()
    boxboard_width = models.FloatField()
    boxboard_height = models.FloatField()
    boxboard_gram = models.FloatField()
    boxboard_rate = models.FloatField()
    boxboard_labour = models.FloatField()
    rolling_cost = models.FloatField()
    additional_labour_cost = models.FloatField()
    printing_cost = models.FloatField()
    lamination_cost = models.FloatField()
    total_cost = models.FloatField()
    total_cost_12 = models.FloatField()
    price_per_copy = models.FloatField()

    def __str__(self):
        return f"{self.customer_name} - {self.paper_width}x{self.paper_height}"