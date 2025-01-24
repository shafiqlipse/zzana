from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    # path("categorys/", Categorys, name="categorys"),
    path("categories/", bCategory, name="categories"),
    path("delete_category/<int:id>", bcategory_delete, name="delete_category"),
    
    # path("categorys/", Categorys, name="categorys"),
    path("genres/", Genres, name="genres"),
    path("delete_genre/<int:id>", genre_delete, name="delete_genre"),
    path("genre/<int:id>", genre_details, name="genre"),
    
    # path("categorys/", Categorys, name="categorys"),
    path("books/", books, name="books"),
    path("delete_book/<int:id>", genre_delete, name="delete_book"),
    path("book/<int:id>", book_details, name="book"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
