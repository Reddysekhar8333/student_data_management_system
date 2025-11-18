
# Create your views here.
from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            Q(name__icontains = query)|
            Q(roll_number__icontains = query)|
            Q(branch__icontains = query)|
            Q(email__icontains = query)
        ).order_by('-created_at')
    else:
        students = Student.objects.all().order_by('-created_at')

    paginator = Paginator(students, 2)  # 2 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'students/students_list.html',
        {'page_obj': page_obj, 'query': query}
    )

@login_required 
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            return redirect("students_list")
    else:
        form = StudentForm()
    return render(request,"students/add_student.html", {"form":form})

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {"form": form})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect("students_list")
