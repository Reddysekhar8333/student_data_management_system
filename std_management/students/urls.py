from django.urls import path
from .views import student_list, add_student, edit_student, delete_student

urlpatterns = [
    path("students/", student_list, name="students_list"),
    path("students/add/", add_student, name="add_student"),
    path("students/<int:student_id>/edit/", edit_student, name="edit_student"),
    path("students/<int:student_id>/delete/", delete_student, name="delete_student"),

]
