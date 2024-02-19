from django.urls import path

from .views import home, logout_user, register_user, custom_record,delete_record,add_record, update_record

urlpatterns = [
    path('home', home, name="home"),    path('logout', logout_user, name="logout"),
    path('register', register_user, name="register"),

    path('add_record', add_record, name="add_record"),

    path('home/record/<int:pk>', custom_record, name="record"),
    path('home/delete_record/<int:pk>', delete_record, name="delete_record"),
    path('home/update_record/<int:pk>', update_record, name="update_record"),


]