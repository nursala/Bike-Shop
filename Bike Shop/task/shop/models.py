from django.db import models


STATUS_CHOICES = [
    ("P", "Pending"),
    ("R", "Ready"),
]


class Frame(models.Model):
    color = models.CharField(max_length=16)
    quantity = models.IntegerField()
    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=16)
    quantity = models.IntegerField()
    def __str__(self):
        return self.color



class Tire(models.Model):
    type = models.CharField(max_length=32)
    quantity = models.IntegerField()
    def __str__(self):
        return self.type



class Basket(models.Model):
    quantity = models.IntegerField()
    def __str__(self):
        return self.quantity



class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    has_basket = models.BooleanField()


class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=16)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
    )