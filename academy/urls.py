"""Urls."""
from django.urls import path

from django.conf.urls import url

from django.conf.urls import include

from . import views

from django.conf import settings

from django.conf.urls.static import static

from django.views.decorators.cache import cache_page

from django.urls import re_path


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('students/', views.view_student, name='view_student'),
    path('lecturers/', views.view_lecturer, name='view_lecturer'),
    path('groups/', views.view_group, name='view_group'),
    path('add_group/', views.add_group, name='add_group'),

    path('edit_students/', cache_page(60 * 5)(views.edit_students), name='edit_students'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    re_path(r'^delete_student/(?P<student_id>[0-9]+)/$', views.delete_student, name='delete_student'),

    path('edit_lecturers/', cache_page(60 * 5)(views.edit_lecturers), name='edit_lecturers'),
    path('lecturers/<int:lecture_id>/edit/', views.edit_lecturer, name='edit_lecturer'),
    re_path(r'^delete_lecturer/(?P<lecture_id>[0-9]+)/$', views.delete_lecturer, name='delete_lecturer'),

    path('edit_groups/', cache_page(60 * 5)(views.edit_groups), name='edit_groups'),
    path('groups/<int:group_id>/edit/', views.edit_group, name='edit_group'),
    re_path(r'^delete_group/(?P<group_id>[0-9]+)/$', views.delete_group, name='delete_group'),

    re_path(r'^silk/', include('silk.urls', namespace='silk')),
    path('contact/', views.contact, name='contact'),
    path('view_contact_message/', views.view_contact_message, name='view_contact_message'),
    path('view_exchange_rate/', views.view_exchange_rate, name='view_exchange_rate'),
    path('users/', include('users.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
