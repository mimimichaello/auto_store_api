from django.db import models
from users.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    release = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.model}'

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models. CharField(max_length=200)

    def __str__(self):
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cars = models.ManyToManyField('Car')
    accessories = models.ManyToManyField('Accessory')
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        car_names = ', '.join([car.name for car in self.cars.all()])
        accessory_names = ', '.join([accessory.name for accessory in self.accessories.all()])
        return f"Корзина для {self.user.username} | Автомобили: {car_names} | Аксессуары: {accessory_names}"
