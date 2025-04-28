from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):

    @property
    def cinema_owner(self):
        try:
            return self.cinemaowner
        except CinemaOwner.DoesNotExist:
            pass

    @property
    def cinema_customer(self):
        try:
            return self.cinemacustomer
        except CinemaCustomer.DoesNotExist:
            pass


class CinemaOwner(models.Model):
    user = models.OneToOneField('User', on_delete=models.PROTECT)


class CinemaCustomer(models.Model):
    user = models.OneToOneField('User', on_delete=models.PROTECT)
