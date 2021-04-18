"""Test views."""
from django.test import TestCase

from django.urls import reverse

from academy.models import Student, Contact

from django.urls import resolve

from django.test import Client


FIRST_NAME = "Artur"
LAST_NAME = "Avdeenko"
EMAIL = "a.avdeenko@ukr.net"


class StudentListViewTest(TestCase):
    """StudentListViewTest."""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData function."""
        student = Student.objects.create(first_name=FIRST_NAME, last_name=LAST_NAME, email=EMAIL)

    def test_view_url_exists_at_desired_location(self):
        """test_view_url_exists_at_desired_location function."""
        resp = self.client.get('/students/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """test_view_url_accessible_by_name function."""
        resp = self.client.get(reverse('view_student'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """test_view_uses_correct_template function."""
        resp = self.client.get(reverse('view_student'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/view_students.html')

    def test_lists_all_students(self):
        """test_lists_all_students function."""
        resp = self.client.get(reverse('view_student'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['students']) == 1)


class ContactViewTest(TestCase):
    """ContactViewTest."""

    @classmethod
    def setUpTestData(cls):
        """setUpTestData function."""
        contact = Contact.objects.create(name=FIRST_NAME, email=EMAIL, message='message')

    def test_view_url_exists_at_desired_location(self):
        """test_view_url_exists_at_desired_location function."""
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """test_view_url_accessible_by_name function."""
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """test_view_uses_correct_template function."""
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/contact.html')

    def test_availability_of_form(self):
        """test_availability_of_form function."""
        resp = self.client.get(reverse('contact'))
        form = resp.context['contact_form']
        self.assertTrue(form)


class AddGroupViewTest(TestCase):
    """AddGroupViewTest."""

    def test_view_url_exists_at_desired_location(self):
        """test_view_url_exists_at_desired_location function."""
        resp = self.client.get('/add_group/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """test_view_url_accessible_by_name function."""
        resp = self.client.get(reverse('add_group'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """test_view_uses_correct_template function."""
        resp = self.client.get(reverse('add_group'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/add_group.html')

    def test_availability_of_form(self):
        """test_availability_of_form function."""
        resp = self.client.get(reverse('add_group'))
        form = resp.context['group_form']
        self.assertTrue(form)
