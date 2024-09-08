# diary_app/urls.py
from django.urls import path
from .views import (
    diary_entries,
    create_entry,
    edit_entry,
    delete_entry,
    logout_view,
    login_view,
    register,
    get_entry,
    add_reply,  # Ensure you have this view
)

urlpatterns = [
    path('', diary_entries, name='diary_entries'),
    path('create/', create_entry, name='create_entry'),
    path('edit/<int:entry_id>/', edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/', delete_entry, name='delete_entry'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('entry/<int:entry_id>/', get_entry, name='get_entry'),
    path('reply/<int:entry_id>/', add_reply, name='add_reply'),  # Ensure this is correct
]