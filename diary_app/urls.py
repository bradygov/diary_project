# diary_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('entries/', views.diary_entries, name='diary_entries'),
    path('entries/create/', views.create_entry, name='create_entry'),
    path('entries/edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('entries/delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('logout/', views.logout_view, name='logout'),
]