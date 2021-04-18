"""Test models."""
from django.test import TestCase

from academy.models import Student, Lecturer, Group

from django.core.exceptions import ValidationError


FIRST_NAME_STUDENT = "Artur"
LAST_NAME_STUDENT = "Avdeenko"
EMAIL_STUDENT = "a.avdeenko@ukr.net"

FIRST_NAME_LECTURER = "Andry"
LAST_NAME_LECTURER = "Bartalenko"
EMAIL_LECTURER = "a.bartalenko@ukr.net"


class StudentModelTest(TestCase):
    """StudentModelTest."""

    @classmethod
    def test_successful_student_creation(self):
        """test_successful_student_creation function."""
        student = Student(first_name=FIRST_NAME_STUDENT, last_name=LAST_NAME_STUDENT, email=EMAIL_STUDENT)
        student.full_clean()

    def test_failure_due_to_long_data_student_name(self):
        """test_failure_due_to_long_data_student_name function."""
        long_data = 'a' * 101
        student = Student(first_name=long_data, last_name=long_data, email=EMAIL_STUDENT)
        expected_message = 'Ensure this value has at most 100 characters (it has 101).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()

    def test_failure_due_to_long_data_student_email(self):
        """test_failure_due_to_long_data_student_email function."""
        long_email = 'a' * 255
        student = Student(first_name=FIRST_NAME_STUDENT, last_name=LAST_NAME_STUDENT, email=long_email)
        expected_message = 'Ensure this value has at most 254 characters (it has 255).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            student.full_clean()


class LecturerModelTest(TestCase):
    """LecturerModelTest."""

    @classmethod
    def test_successful_lecturer_creation(self):
        """test_successful_lecturer_creation function."""
        lecturer = Lecturer(first_name=FIRST_NAME_LECTURER, last_name=LAST_NAME_LECTURER, email=EMAIL_LECTURER)
        lecturer.full_clean()

    def test_failure_due_to_long_data_lecturer_name(self):
        """test_failure_due_to_long_data_lecturer_name function."""
        long_data = 'a' * 101
        lecturer = Lecturer(first_name=long_data, last_name=long_data, email=EMAIL_LECTURER)
        expected_message = 'Ensure this value has at most 100 characters (it has 101).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()

    def test_failure_due_to_long_data_lecturer_email(self):
        """test_failure_due_to_long_data_lecturer_email function."""
        long_email = 'a' * 255
        lecturer = Lecturer(first_name=FIRST_NAME_LECTURER, last_name=LAST_NAME_LECTURER, email=long_email)
        expected_message = 'Ensure this value has at most 254 characters (it has 255).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            lecturer.full_clean()


class GroupModelTest(TestCase):
    """GroupModelTest."""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData function."""
        cls.course = '116'

    def setUp(self) -> None:
        """setUp function."""
        self.teacher = Lecturer(first_name=FIRST_NAME_LECTURER, last_name=LAST_NAME_LECTURER, email=EMAIL_LECTURER)
        self.student = Student(first_name=FIRST_NAME_STUDENT, last_name=LAST_NAME_STUDENT, email=EMAIL_STUDENT)
    
    def test_successful_group_creation(self):
        """test_successful_group_creation function."""
        group = Group.objects.create(course=self.course)
        group.save()
        group.teacher=self.teacher.pk
        group.students.set([self.student.pk])
        group.save()

    def test_failure_due_to_long_data_course_name(self):
        """test_failure_due_to_long_data_course_name function."""
        long_course_name = 'a' * 101
        group = Group.objects.create(course=long_course_name)
        group.save()
        expected_message = 'Ensure this value has at most 100 characters (it has 101).'
        with self.assertRaisesMessage(ValidationError, expected_message):
            group.full_clean()
            