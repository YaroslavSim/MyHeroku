"""Append data."""
from django.core.management.base import BaseCommand

from faker import Faker

from ...models import Group, Lecturer, Student


class Command(BaseCommand):
    """Append_data_class."""

    def add_arguments(self, parser):
        """Argument_pareser."""
        parser.add_argument('total', type=int, help='Indicates the number of groups to be created')

    def handle(self, *args, **kwargs):
        """Data_append_function."""
        fake = Faker()
        total = kwargs['total']
        for i in range(total):
            lecturer = Lecturer(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email())
            lecturer.save()
            group = Group(course=fake.job(), teacher=lecturer)
            group.save()
            for j in range(10):
                student = Student(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email())
                student.save()
                group.students.add(student)