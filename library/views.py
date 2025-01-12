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
def Genres(request):
    genres = Genre.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = GenreForm()

    context = {
        "form": form,
        "genres": genres,
        "form_errors": form_errors,
    }
    return render(request, "books/genres.html", context)


@login_required(login_url="login")
def genre_delete(request, id):
    stud = Genre.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("genres")

    return render(request, "books/delete_genre.html", {"obj": stud})

# Create your views here.


def genre_details(request, id):
    genre = get_object_or_404(Genre, id=id)
    
    context = {
        "genre": genre,

    }
    return render(request, "books/genre.html", context)
