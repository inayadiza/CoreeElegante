from django.urls import path
from main.views import show_main, create_clothing_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user,logout_user
from main.views import edit_clothing, delete_clothing, show_clothing, add_clothing_entry_ajax
from . import views

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-clothing-entry', create_clothing_entry, name='create_clothing_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-clothing/<uuid:id>', edit_clothing, name='edit_clothing'),
    path('delete/<uuid:id>', delete_clothing, name='delete_clothing'),
    path('clothing/', show_clothing, name='show_clothing'),
    path('create-clothing-entry-ajax', add_clothing_entry_ajax, name = 'add_clothing_entry_ajax'),
]