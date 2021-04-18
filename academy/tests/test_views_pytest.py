"""Test views pytest."""
from academy.models import Student, Contact, Lecturer

import pytest

from django.urls import reverse

from academy.tests.factory import UserFactory


FIRST_NAME = "Artur"
LAST_NAME = "Avdeenko"
EMAIL = "a.avdeenko@ukr.net"


@pytest.mark.django_db
def test_user_creation():
    user = Student.objects.create(first_name=FIRST_NAME, last_name=LAST_NAME, email=EMAIL)
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_view_students_url_exists_at_desired_location(client):
    resp = client.get('/students/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_unauthorized(client):
    response = client.get('/admin/academy/student/')
    assert response.status_code == 302
    assert '/admin/login/' in response.url


@pytest.mark.django_db
def test_superuser_view(admin_client):
    response = admin_client.get('/admin/academy/student/')
    assert response.status_code == 200


@pytest.fixture
def student():
    return Student.objects.create(first_name=FIRST_NAME, last_name=LAST_NAME, email=EMAIL)


@pytest.mark.django_db
def test_lists_all_students(client, student):
    resp = client.get(reverse('view_student'))
    assert resp.status_code == 200
    assert len(resp.context['students']) == 1


@pytest.fixture
def create_students(django_user_model):
    def make_students(**kwargs):
        number_of_students = kwargs['number_of_students']
        students = []
        for student_num in range(number_of_students):
            student = Student.objects.create(
                first_name=f'{str(student_num)}',
                last_name=f'{str(student_num)}',
                email=f'{str(student_num)}@gmail.com'
            )
            students.append(student)
        return students
    return make_students


@pytest.mark.django_db
def test_lists_all_students(client, create_students):
    number_of_students = 4
    create_students(number_of_students=number_of_students)

    resp = client.get(reverse('view_student'))
    assert resp.status_code == 200

    articles = resp.context['students']
    assert len(articles) == number_of_students


@pytest.mark.django_db
def test_hide_edit_button_for_not_authenticated_user(client, create_students):
    students = create_students(number_of_students=1)
    student = students[0]
    resp = client.get(reverse('edit_students'))
    assert resp.status_code == 200
    expected_link = f'<a href="/students/{student.student_id}/edit/">'
    assert expected_link.encode() not in resp.content


@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        return UserFactory.create(**kwargs)
    return make_user


@pytest.fixture
def auto_login_user(client, create_user):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.force_login(user)
        return client, user
    return make_auto_login


@pytest.mark.django_db
def test_show_edit_button_for_authenticated_user(client, auto_login_user, create_students):
    students = create_students(number_of_students=4)
    student = students[0]
    client, user = auto_login_user()
    resp = client.get(reverse('edit_students'))
    assert resp.status_code == 200
    expected_link = f'<a href="/students/{student.student_id}/edit/">'
    #assert expected_link.encode() in resp.content


############### StudentListViewTest #################################
@pytest.mark.django_db
def test_view_url_exists_at_desired_location_student_list(client):
    resp = client.get('/students/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name_student_list(client):
    resp = client.get(reverse('view_student'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_lists_all_students_student_list(client):
    resp = client.get(reverse('view_student'))
    assert resp.status_code == 200
    #assert len(resp.context['students']) == 1


############### ContactViewTest #################################
@pytest.mark.django_db
def test_view_url_exists_at_desired_location_contact_view(client):
    resp = client.get('/contact/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name_contact_view(client):
    resp = client.get(reverse('contact'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_availability_of_form_contact_view(client):
    resp = client.get(reverse('contact'))
    assert resp.context['contact_form']


################# AddGroupViewTest ################################
@pytest.mark.django_db
def test_view_url_exists_at_desired_location(client):
    resp = client.get('/add_group/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name(client):
    resp = client.get(reverse('add_group'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_availability_of_form(client):
    resp = client.get(reverse('add_group'))
    assert resp.context['group_form']


################# OtherTest ################################
@pytest.mark.django_db
def test_view_url_exists_at_desired_location(client):
    resp = client.get('/view_exchange_rate/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name(client):
    resp = client.get(reverse('view_exchange_rate'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_availability_of_exchange_rate(client):
    resp = client.get(reverse('view_exchange_rate'))
    assert b'View exchange rate' in resp.content
    assert b'Exchange rate' in resp.content
#############################################################


@pytest.mark.django_db
def test_view_url_exists_at_desired_location(client):
    resp = client.get('/view_contact_message/')
    assert resp.status_code == 200


@pytest.fixture
def create_contact_message(django_user_model):
    def make_contact_messages(**kwargs):
        number_of_contact_messages = kwargs['number_of_contact_messages']
        contact_messages = []
        for contact_message_num in range(number_of_contact_messages):
            contact_message = Contact.objects.create(
                name=f'{str(contact_message_num)}',
                message='some text',
                email=f'{str(contact_message_num)}@gmail.com'
            )
            contact_messages.append(contact_message)
        return contact_messages
    return make_contact_messages


@pytest.mark.django_db
def test_availability_of_contact_messages(client, create_contact_message):
    contact_messages = create_contact_message(number_of_contact_messages=4)
    resp = client.get('/view_contact_message/')
    assert len(resp.context['contact_messages']) == 4
######################################################################

@pytest.mark.django_db
def test_view_url_exists_at_desired_location(client):
    resp = client.get('/lecturers/')
    assert resp.status_code == 200


@pytest.fixture
def create_lecturers(django_user_model):
    def make_lecturers(**kwargs):
        number_of_lecturers = kwargs['number_of_lecturers']
        lecturers = []
        for lecturer_num in range(number_of_lecturers):
            lecturer = Lecturer.objects.create(
                first_name=f'{str(lecturer_num)}',
                last_name=f'{str(lecturer_num)}',
                email=f'{str(lecturer_num)}@gmail.com',
                cover = 'covers/default.png'
            )
            lecturers.append(lecturer)
        return lecturers
    return make_lecturers


@pytest.mark.django_db
def test_availability_of_lecturers_list(client, create_lecturers):
    lecturers = create_lecturers(number_of_lecturers=5)
    resp = client.get('/lecturers/')
    assert len(resp.context['lecturers']) == 5