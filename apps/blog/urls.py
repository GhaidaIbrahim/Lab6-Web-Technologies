from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search', views.search, name='books.search'),
    path('add-book-now/', views.some_view_function, name='add_book_test'),
    path('simple/query', views.simple_query),
    path('complex/query', views.lookup_query),
]