from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('record/<int:pk>', views.record_user, name='record_user'),
    path('record/delete/<int:pk>', views.delete_record, name='delete_record'),
    path('record/add', views.add_record, name='add_record'),
    path('record/update/<int:pk>', views.update_record, name='update_record'),
]
