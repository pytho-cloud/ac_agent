from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

STAR_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
class AC(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('refurbished', 'Refurbished'),
    ]

    TYPE_CHOICES = [
        ('window', 'Window AC'),
        ('split', 'Split AC'),
        ('four_way_cassette', '4 Way Cassette AC'),
        ('one_way_cassette', 'One Way Cassette AC'),
        ('tower', 'Tower AC'),
        ('ductable', 'Ductable AC'),
        ('hvac', 'HVAC'),
        ('vrf', 'VRF System'),
        ('vrv', 'VRV System'),
    ]

    ton = models.CharField(max_length=255,null=True)

    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    ac_types = MultiSelectField(choices=TYPE_CHOICES, max_length=255, blank=True, null=True)
    capacity = models.DecimalField(max_digits=3, decimal_places=1)  # 1.5
    energy_rating = models.IntegerField()  # 3,4,5
    price = models.IntegerField()
    description  = models.TextField(null= True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="ac-images/",null=True)
    is_home_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
    


class ACImage(models.Model):
    ac = models.ForeignKey(
        AC,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="ac-images/")

    def __str__(self):
        return f"Image for {self.ac.model_name}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)

    STAR_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    star = models.IntegerField(choices=STAR_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product_name} ({self.star}⭐)"


# models.py

class Maintainence(models.Model):
    title = models.CharField(max_length=100,null=True)              # Name of the service
    description = models.TextField(null=True)                      # Description
    icon = models.CharField(max_length=50,null=True)               # Store FontAwesome icon name like "faSnowflake"
    is_active = models.BooleanField(default=True,null=True)        # Whether to show this service

    def __str__(self):
        return self.title




class Reviews(models.Model):
    name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255,null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=STAR_CHOICES)
    image = models.ImageField(upload_to='review/images')
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}--{self.review}'



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class BookService(models.Model):

    full_name = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    service_requirements = models.TextField()



    def __str__(self):
        return f"{self.full_name}--{self.phone_number}"


    
class ProductSell(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    product_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.product_name}'



class ProductSellImages(models.Model):
    product = models.ForeignKey(ProductSell, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to="product-sell/")
    images_created_at = models.DateTimeField(auto_now_add=True)
