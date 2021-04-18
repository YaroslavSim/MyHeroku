"""Models."""
from django.db import models


class Student(models.Model):
    """Student class."""

    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    cover = models.ImageField(upload_to='covers/', default='covers/default.png')


class Lecturer(models.Model):
    """Lecturer class."""

    lecture_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    cover = models.ImageField(upload_to='covers/', default='covers/default.png')


class Group(models.Model):
    """Group class."""

    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank=True)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)


class Contact(models.Model):
    """Contact class."""

    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'message': self.message
        }