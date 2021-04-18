"""Test forms."""
from academy.forms import StudentForm

def test_student_form_validation():
    form_data = {'first_name': 'a' * 90, 'last_name': 'some text', 'email': 'some_email@some_domain.com'}
    form = StudentForm(data=form_data)
    assert form.is_valid() is True


def test_student_validation_failure():
    form_data = {'first_name': 'a' * 101, 'last_name': 'some text', 'email': 'some_email@some_domain.com'}
    form = StudentForm(data=form_data)
    assert form.is_valid() is False
