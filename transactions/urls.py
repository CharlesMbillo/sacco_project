from django.urls import path
from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.index, name='index'),
    path('summary/', views.transaction_summary, name='summary'),
    path('html/', views.transaction_html, name='transaction_html'),
    path('csv/', views.transaction_csv, name='transaction_csv'),
    path('pdf/', views.transaction_pdf, name='transaction_pdf'),
]
