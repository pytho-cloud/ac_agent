from django.db import models

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
        ('split', 'Split'),
        ('window', 'Window'),
    ]
    ton = models.CharField(max_length=255,null=True)

    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    ac_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    capacity = models.DecimalField(max_digits=3, decimal_places=1)  # 1.5
    energy_rating = models.IntegerField()  # 3,4,5
    price = models.IntegerField()
    description  = models.TextField(null= True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="ac-images/",null=True)
    is_home_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
    



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


class Maintainence(models.Model):
    icon = models.CharField(max_length =255,null=True,blank=True)
    description = models.TextField()
    price = models.CharField(max_length=255)
    star = models.IntegerField(choices=STAR_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description



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