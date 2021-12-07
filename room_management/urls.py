from . import views
from django.urls import path

app_name = 'sample'

urlpatterns = [
    path('', views.index, name='index'),
    path('exit_ok', views.exit_ok, name='exit_ok'),
    path('home', views.home, name='home'),
    path('out_confirmation', views.out_confirmation, name='out_confirmation'),
    path('logout_ok', views.logout_ok, name='logout_ok'),
    path('in_confirmation', views.in_confirmation, name='in_confirmation'),
    path('in_ok', views.in_ok, name='in_ok'),
    path('qr_reading', views.qr_reading, name='qr_reading')
]