from django.shortcuts import render
from .models import Book
def index(request):
    return render(request, "index.html") 
def list_books(request):
    return render(request, 'list_books.html')
def viewbook(request, bookId):
    return render(request, 'one_book.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def search(request):
    return render(request, 'blog/search.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        
        return render(request, 'blog/bookList.html', {'books':newBooks})

def some_view_function(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return render(request, 'blog/search.html')
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'blog/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    
    if len(mybooks) >= 1:
        return render(request, 'blog/bookList.html', {'books': mybooks})
    else:
        return render(request, 'index.html')