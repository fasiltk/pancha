from django.db import models

# Create your models here.


class Labour(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    profession = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    fees = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address=models.TextField()
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    book = models.ForeignKey(Customer, on_delete=models.CASCADE)
    labour_username=models.CharField(max_length=100)
    booking_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"Customer: {self.book.name} Labour: {self.labour_username}"