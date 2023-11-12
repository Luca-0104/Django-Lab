from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # (use str Class name only when you have to)
    # solve the cycle relation ship using related_name
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Cart(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Sliver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed")
    ]

    place_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    # one to many (1 customer -> n orders)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)    
    # one to many (1 collection -> n product)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # many to many
    promotions = models.ManyToManyField(Promotion)


class CartItem(models.Model):
    # one to many (1 Cart -> n CartItem)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # one to many (1 Product -> n CartItem)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()


class OrderItem(models.Model):
    # one to many (1 Order -> n OrderItem)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # one to many (1 Product -> n OrderItem)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # one to one relation with Customer
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    # one to many (One customer -> many Address)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
