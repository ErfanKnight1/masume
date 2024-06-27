from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL


class Customer(models.Model):
  user = models.ForeignKey(User, verbose_name="مالک", on_delete=models.CASCADE)
  name=models.CharField(max_length=225,verbose_name="نام و نام خوانوادگی")
  phone=models.IntegerField(verbose_name="شماره تماس",null=True)
  email=models.EmailField(max_length=100,verbose_name="ایمیل")
  text=models.TextField(max_length=1000000,verbose_name="پیام")
  
  class Meta:
    verbose_name="مشتری"
    verbose_name_plural="مشتری ها"

  def __str__ (self):
    return self.user.username

  
class Profile(models.Model):
  user = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)
  name=models.CharField(max_length=225,verbose_name="نام و نام خوانوادگی")
  phone=models.IntegerField(verbose_name="شماره تماس",null=True)
  email=models.EmailField(max_length=100,verbose_name="ایمیل")
  text=models.TextField(max_length=1000000,verbose_name="رزومه")
  
  class Meta:
    verbose_name="کاربرها"
    verbose_name_plural="کاربر ها"

  def __str__ (self):
    return self.user.username

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    DateandTime = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1024, blank=True)
    answer = models.CharField(max_length=1024, blank=True)


class Resume(models.Model):
  user = models.ForeignKey(User, on_delete=CASCADE)
  
  name  = models.CharField(max_length=16, blank=True)
  phone_number  = models.CharField(max_length=16, blank=True)
  age  = models.CharField(max_length=16, blank=True)
  coop_type = models.CharField(max_length=16, blank=True)
  more_details = models.CharField(max_length=1024, blank=True)