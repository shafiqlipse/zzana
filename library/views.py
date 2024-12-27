from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def bCategory(request):
    categories = BookCategory.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = BookCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = BookCategoryForm()

    context = {
        "form": form,
        "categories": categories,
        "form_errors": form_errors,
    }
    return render(request, "books/categories.html", context)


@login_required(login_url="login")
def bcategory_delete(request, id):
    stud = BookCategory.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("departments")

    return render(request, "books/delete_category.html", {"obj": stud})

# Create your views here.


@login_required(login_url="login")
def Subjects(request):
    subjects = Subject.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = SubjectForm()

    context = {
        "form": form,
        "subjects": subjects,
        "form_errors": form_errors,
    }
    return render(request, "books/subjects.html", context)


@login_required(login_url="login")
def subject_delete(request, id):
    stud = Subject.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("subjects")

    return render(request, "books/delete_subject.html", {"obj": stud})

# Create your views here.


def subject_details(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.subject = subject
            paper.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = BookCategoryForm()
    context = {
        "subject": subject,
        "form": form,
        "papers": subject.paper_set.all(),
        # "form_errors": form_errors,
    }
    return render(request, "books/subject.html", context)
