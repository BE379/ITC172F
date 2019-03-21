from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# student, class, schedule

class Student(models.Model):
    studentname=models.CharField(max_length=255)
    studentemail=models.EmailField(max_length=255)

    def __str__(self):
        return self.studentname

    class Meta:
        db_table='student'

class Classes(models.Model):
    classname=models.CharField(max_length=100)
    classid=models.CharField(max_length=15)
    classinstructor=models.CharField(max_length=75)
    classtime=models.TimeField()
    classdescription=models.TextField()

    def __str__(self):
        return self.classname

    class Meta:
        db_table='classes'

class Schedule(models.Model):
    studentid=models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    classid=models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    schedulecomments=models.TextField()

    def __str__(self):
        return self.schedulecomments

    class Meta:
        db_table='schedule'

    