from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')


# class ModelBase(models.Model):
#     name = models.CharField(max_length=15, unique=True)
#
#     class Meta:
#         abstract = True
#
#
# class Ticket(models.Model):
#     name = models.CharField(max_length=15, unique=True)
#     booking_date = models.DateField(auto_now_add=True)
#     user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
#
#
# class Ticket_details(models.Model):
#     seats = models.IntegerField()
#     note = models.CharField(max_length=50)
#     ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL)
#
#
# class TuyenXe(ModelBase):
#     point_of_departure = models.CharField(max_length=20, unique=False)
#     destination = models.CharField(max_length=20, unique=False)
#     pricelist = models.IntegerField()
#     ticket_details = models.ForeignKey(Ticket_details, null=True, on_delete=models.SET_NULL)
#
#
# # class Range_of_vehicle(ModelBase):
# #
# #     def __str__(self):
# #         return self.name
#
#
# class Car(ModelBase):
#     license_plate = models.CharField(max_length=15, unique=True)
#     number_of_seats = models.IntegerField()
#     ticket_details = models.ForeignKey(Ticket_details, null=True, on_delete=models.SET_NULL)
#     # Range_of_vehicle = models.ForeignKey(Range_of_vehicle, on_delete = models.SET_NULL)
#
#     def __str__(self):
#         return self.name
