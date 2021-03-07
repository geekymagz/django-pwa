from django.urls import path
from mywebsite.views import index

app_name = 'mywebsite'

urlpatterns = [
    path('', index.as_view(), name='index'),
]