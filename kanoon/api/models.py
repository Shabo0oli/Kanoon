from django.db import models
from django.contrib.auth.models import User
from awesome_avatar.fields import AvatarField
from phonenumber_field.modelfields import PhoneNumberField
from django_jalali.db import models as jmodels


# Create your models here.

class Kanoon(models.Model):

    Name = models.CharField(max_length=40)
    Logo = AvatarField(upload_to='logos', width=100, height=100 , null=True , blank=True)
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
    # PhoneNumber = models.CharField(max_length=20)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    isValid = models.BooleanField(default=False)
    Avatar = AvatarField(upload_to='Leaders', width=100, height=100,  null=True , blank=True)
    PhoneNumber = PhoneNumberField()
    Email = models.EmailField(max_length=70,unique=True , blank=True , null=True)

    def __str__(self):
        return '{} - {}'.format(self.Username, self.Fullname)


class Member(models.Model):

    FirstName = models.CharField(max_length=30 , blank=True)
    LastName = models.CharField(max_length=30 , blank=True)
    NickName = models.CharField(max_length=30 , blank=True)
    # PhoneNumber = models.CharField(max_length=20)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    objects = jmodels.jManager()
    BrithDate = jmodels.jDateField(blank=True , null=True)
    PhoneNumber = PhoneNumberField()
    Avatar = AvatarField(upload_to='Members', width=100, height=100, null=True , blank=True)
    Group = models.ManyToManyField(Group)
    Email = models.EmailField(max_length=70,unique=True,blank=True , null=True)

    def __str__(self):
        return '{} - {}'.format(self.FirstName, self.LastName)


class Event(models.Model):

    Name = models.CharField(max_length=40)
    Kanoon = models.ForeignKey(Kanoon, on_delete=models.CASCADE)
    objects = jmodels.jManager()
    DateTime = jmodels.jDateTimeField
    Group = models.ManyToManyField(Group)  # TODO: Only from Kanoon Group
    Creator = models.ForeignKey(User, on_delete=models.CASCADE)  # TODO : default current user
    Description = models.TextField()
    Members = models.ManyToManyField(Member)    # TODO: Only from Group Member
    Poster = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.Name, self.Kanoon)




