from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(_('teacher name'), max_length=100)

    # def get_absolute_url(self):
    #     return reverse('teacher-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.teacher_name

class ClassRoom(models.Model):
    class_room = models.CharField(_('class room'), max_length=20)
    day_of_week = models.CharField(_('day of week'), max_length=20)
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    
    #To display today's classroom only
    def today_classes(self):
        today = datetime.datetime.now().date()
        day = today.strftime('%A')   
        if self.day_of_week == day:
            return self.class_room
           
    def duration(self):
        d_start = datetime.datetime.combine(datetime.date.today(), self.start_time)
        d_end = datetime.datetime.combine(datetime.date.today(), self.end_time)
        duration_class = d_end - d_start
        return duration_class

    def __str__(self):
        return self.class_room

    # def get_absolute_url(self):
    #     return reverse('classroom-detail-view', args=[str(self.id)])


class Member(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']

    # def get_absolute_url(self):
    #     return reverse('member-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.user.username

class Checkout(models.Model):
    CHOICES = (
    ('1', 'Dropoff'),
    ('2', 'Pickup'),
)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    checkout_choice = models.CharField(_('checkout choice'), max_length=100, choices=CHOICES)
    checkout_time = models.DateTimeField(_('checkout time'), auto_now_add=True)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)

  


    

    

