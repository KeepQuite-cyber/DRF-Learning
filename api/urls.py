from django.urls import path
from . import views
urlpatterns = [
    path("students/" , views.studentView),
    path("students/<int:pk>/" , views.studentDetailView),

    path("employees/", views.Employees.as_view())
]
