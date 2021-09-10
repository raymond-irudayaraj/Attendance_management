from django.contrib.auth.models import User
from django.db import models
from users.models import User

# Create your models here.

class Schedule(models.Model):
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.teacher.first_name + ' '+ str(self.start_time)

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.BooleanField(null=True, default=False) # 0 - logged out | 1 - logged in
    time = models.DateTimeField(auto_now=True, auto_now_add=False)
    classid = models.ForeignKey(Schedule, on_delete=models.CASCADE) 
    active_time = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.user.first_name