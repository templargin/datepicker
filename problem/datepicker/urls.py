from django.urls import path

from . import views

app_name = 'datepicker'
urlpatterns = [

    path('', views.index, name='index'),
    path('regular', views.RegularForm.as_view(), name='regular'),
    path('modal', views.modal, name='modal'),
    path('create/', views.ContactCreateView.as_view(), name='create_contact'),



]
