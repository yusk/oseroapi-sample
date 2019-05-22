from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('api/osero/', views.OseroView.as_view(), name="osero"),
]
