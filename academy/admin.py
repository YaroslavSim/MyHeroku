"""Admin."""
from django.contrib import admin
from django.db import models
from django.http import HttpResponse
from .models import Group, Lecturer, Student, Contact
import csv


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """StudentAdmin class."""

    actions = ['export']
    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student.csv"'
        writer = csv.writer(response)
        header = ['student_id', 'first_name', 'last_name', 'email']
        writer.writerow(header)
        for student in queryset:
            row = [
                student.student_id, 
                student.first_name, 
                student.last_name, 
                student.email
                ]
            writer.writerow(row)
        return response

    export.short_description = 'Export student'


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    """LecturerAdmin class."""

    actions = ['export']
    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lecturer.csv"'
        writer = csv.writer(response)
        header = ['lecture_id', 'first_name', 'last_name', 'email']
        writer.writerow(header)
        for lecturer in queryset:
            row = [
                lecturer.lecture_id, 
                lecturer.first_name, 
                lecturer.last_name, 
                lecturer.email
                ]
            writer.writerow(row)
        return response

    export.short_description = 'Export lecturer'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """GroupAdmin class."""

    actions = ['export']
    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="group.csv"'
        writer = csv.writer(response)
        header = ['group_id', 'course', 'students', 'teacher']
        writer.writerow(header)
        for group in queryset:
            row = [
                group.group_id, 
                group.course, 
                group.students, 
                group.teacher
                ]
            writer.writerow(row)
        return response

    export.short_description = 'Export group'


admin.site.register(Contact)
