"""Signals."""
import os

from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver

from .models import Group, Lecturer, Student, Contact

from .tasks import send_email


@receiver(pre_save, sender=Student)
def capitalize_name_student(sender, instance, **kwargs):
    """Student pre_save function."""
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Lecturer)
def capitalize_name_lecturer(sender, instance, **kwargs):
    """Lecturer pre_save function."""
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Group)
def capitalize_name_group(sender, instance, **kwargs):
    """Group pre_save function."""
    instance.course = instance.course.capitalize()


@receiver(post_save, sender=Contact)
def send_notification(sender, instance, **kwargs):
    """Send email post_save function."""
    send_email.delay(instance.to_dict())
