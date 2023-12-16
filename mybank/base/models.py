# pylint: disable=missing-class-docstring
from email.policy import default
from enum import auto
from venv import create
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime    
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
 

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=20)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by =models.ForeignKey(User,on_delete=models.CASCADE)

    gifLink = models.TextField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Days(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Lectures(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    days_of_lec = models.ManyToManyField(Days)
    earned_point = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)
    lecture = models.ForeignKey(Lectures,  null=True, blank=True,on_delete=models.SET_NULL,related_name="activities")
    is_grade = models.BooleanField(default=False)
    weight = models.IntegerField(default=0,validators=[MaxValueValidator(100), MinValueValidator(0)],null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_high_priority = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title if self.title else "Untitled"


    class Meta:
        ordering = [ 'created_at']


class Studies(models.Model):
    title = models.CharField(max_length=400)
    lecture = models.ForeignKey(Lectures,  null=True, blank=True,on_delete=models.SET_NULL,related_name="studies")
    how_many_minutes = models.IntegerField(default=1,validators=[MaxValueValidator(6000), MinValueValidator(0)],null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']        

class Grades(models.Model):

    grade = models.IntegerField( validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    activity = models.ForeignKey(Activity,  null=True, blank=True,on_delete=models.SET_NULL,related_name="grade")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.activity.title

    class Meta:
        ordering = ['created_at']

class TransferCodes(models.Model):
    code = models.CharField(max_length=200,default="000000")
    hall = models.CharField(max_length=200,default="A")
    meal = models.CharField(max_length=200,default="aksam")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.code+" "+self.hall+" "+self.meal

    class Meta:
        ordering = ['created_at']


    

