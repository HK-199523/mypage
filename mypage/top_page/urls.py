from django.urls import path
from . import views

app_name = 'top_page'


urlpatterns = [
    path('top',views.IndexView.as_view(),name = 'index'),
]
