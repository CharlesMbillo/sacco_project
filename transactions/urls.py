from django.urls import path 
from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.index, name='index'),
    path('summary_template/', views.transaction_summary, name='summary_template'),
    path('html/', views.transaction_html, name='transaction_html'),
    path('csv/', views.transaction_csv, name='transaction_csv'),
    path('pdf/', views.transaction_pdf, name='transaction_pdf'),
    path('success/', views.success, name='success.html')
]
