"""Views."""
from django.shortcuts import render,redirect

from django.shortcuts import get_object_or_404

from .models import Group, Lecturer, Student, Contact

from .forms import StudentForm, LecturerForm, GroupForm, ContactForm

from exchanger.models import ExchangeRate

from django.views.decorators.cache import cache_page

from django.contrib.auth.decorators import login_required


def view_student(request):
    """Student selection function."""
    students = Student.objects.all()
    return render(request, 'academy/view_students.html', {'students': students})


def view_lecturer(request):
    """Lecturer selection function."""
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/view_lecturers.html', {'lecturers': lecturers})


def view_group(request):
    """Group selection function."""
    groups = Group.objects.all()
    return render(request, 'academy/view_groups.html', {'groups': groups})


def add_group(request):
    """Group add function."""
    new_group = None
    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=False)
            new_group.save()
    context = {
        'group_form': GroupForm(),
        'new_group': new_group
    }
    return render(request, 'academy/add_group.html', context)


def edit_students(request):
    """Students edit function."""
    students = Student.objects.all().order_by('-first_name')
    new_student = None
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            new_student.save()
    context = {
        'students': students,
        'student_form': StudentForm(),
        'new_student': new_student
    }
    return render(request, 'academy/edit_students.html', context)


#@login_required
def edit_student(request, student_id):
    """Student edit function."""
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('edit_students')

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_student.html', {'form': form})


def delete_student(request, student_id):
    """Student delete function."""
    student = get_object_or_404(Student, student_id=student_id)
    if student_id:
        student.delete()
        return redirect('edit_students')
    students = Student.objects.all()
    return render(request, 'academy/view_students.html', {'students': students})


def edit_lecturers(request):
    """Lecturers edit function."""
    lecturers = Lecturer.objects.all().order_by('-first_name')
    new_lecturer = None
    if request.method == 'POST':
        lecturer_form = LecturerForm(data=request.POST)
        if lecturer_form.is_valid():
            new_lecturer = lecturer_form.save(commit=False)
            new_lecturer.save()
    context = {
        'lecturers': lecturers,
        'lecturer_form': LecturerForm(),
        'new_lecturer': new_lecturer
    }
    return render(request, 'academy/edit_lecturers.html', context)


def edit_lecturer(request, lecture_id):
    """Lecturer edit function."""
    lecturer = get_object_or_404(Lecturer, lecture_id=lecture_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.save()
            return redirect('edit_lecturers')

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_lecturer.html', {'form': form})


def delete_lecturer(request, lecture_id):
    """Lecturer delete function."""
    lecturer = get_object_or_404(Lecturer, lecture_id=lecture_id)
    if lecture_id:
        lecturer.delete()
        return redirect('edit_lecturers')
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/view_lecturers.html', {'lecturers': lecturers})


def edit_groups(request):
    """Groups edit function."""
    groups = Group.objects.all()
    new_group = None
    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=False)
            new_group.save()
    context = {
        'groups': groups,
        'group_form': GroupForm(),
        'new_group': new_group
    }
    return render(request, 'academy/edit_groups.html', context)


def edit_group(request, group_id):
    """Group edit function."""
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('edit_groups')

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_group.html', {'form': form})


def delete_group(request, group_id):
    """Group delete function."""
    group = get_object_or_404(Group, group_id=group_id)
    if group_id:
        group.delete()
        return redirect('edit_groups')
    groups = Group.objects.all()
    return render(request, 'academy/view_groups.html', {'groups': groups})


def contact(request):
    """Contact function."""
    new_contact = None
    sender = request.session.get('sender')
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            if new_contact.email not in sender:
                new_contact.save()
                if sender:
                    request.session['sender'].append(new_contact.email)
                else:
                    request.session['sender'] = [new_contact.email]
                request.session.modified = True
    context = {
        'contact_form': ContactForm(),
        'new_contact': new_contact,
        'sender': request.session.get('sender')
    }
    return render(request, 'academy/contact.html', context)


def view_contact_message(request):
    """Contact message selection function."""
    contact_messages = Contact.objects.all()
    return render(request, 'academy/view_contact_message.html', {'contact_messages': contact_messages})


def view_exchange_rate(request):
    """Exchange Rate selection function."""
    exchange_rates = ExchangeRate.objects.all()
    context = {
        k: v for ex_rate in exchange_rates
        for k, v in ex_rate.to_dict().items()
    }
    return render(request, 'academy/view_exchange_rate.html', context)