"""Test forms."""
from django.test import TestCase

from academy.forms import StudentForm

class StudentFormTest(TestCase):
    """StudentFormTest."""

    def test_expected_fields(self):
        """Test_expected_fields function."""
        form = StudentForm()
        expected_fields = {'first_name', 'last_name', 'email'}
        self.assertEqual(set(form.fields.keys()), expected_fields)

    def test_title_validation_failure(self):
        """Test_title_validation_failure function."""
        form_data = {'first_name': 'a' * 101, 'last_name': 'some text', 'email': 'some_email@some_domain.com'}
        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())