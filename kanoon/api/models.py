from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Kanoon(models.Model):

    Name = models.CharField(max_length=40)
    # TODO :  Logo
    FoundationDate = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.Name)


class Group(models.Model):

    Name = models.CharField(max_length=40)
    Kanoon = models.ForeignKey(Kanoon , on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.Name , self.Kanoon)


class Leader(models.Model):

    Username = models.OneToOneField(User , on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=100 , blank=True)
    PhoneNumber = models.CharField(max_length=20)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    isValid = models.BooleanField(default=False)
    # TODO : avatar , Email , Phone number

    def __str__(self):
        return '{} - {}'.format(self.Username, self.Fullname)


class Member(models.Model):

    FirstName = models.CharField(max_length=30 , blank=True)
    LastName = models.CharField(max_length=30 , blank=True)
    NickName = models.CharField(max_length=30 , blank=True)
    PhoneNumber = models.CharField(max_length=20)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    # TODO : avatar , Email , Phone number , BirthDate ,
    Group = models.ManyToManyField(Group)

    def __str__(self):
        return '{} - {}'.format(self.FirstName, self.LastName)


class Event(models.Model):

    Name = models.CharField(max_length=40)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    # TODO : Jalali Date
    Group = models.ManyToManyField(Group)  # TODO: Only from Kanoon Group
    Creator = models.ForeignKey(User, on_delete=models.CASCADE)  # TODO : default current user
    Description = models.TextField()
    Members = models.ManyToManyField(Member)    # TODO: Only from Group Member
    # TODO :Time , Desc , Poster

    def __str__(self):
        return '{} - {}'.format(self.Name, self.Kanoon)




