from django.db import models

# Create your models here.
class AC(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('refurbished', 'Refurbished'),
    ]

    TYPE_CHOICES = [
        ('split', 'Split'),
        ('window', 'Window'),
    ]

    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    ac_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    capacity = models.DecimalField(max_digits=3, decimal_places=1)  # 1.5
    energy_rating = models.IntegerField()  # 3,4,5
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

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
