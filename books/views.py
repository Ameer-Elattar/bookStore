from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from books.models import Book
from books.forms import bookForm,bookModelform

# Create your views here.

def aboutUs(req):
    return render(req, "books/aboutUs.html")


def contactUs(req):
    return render(req, "books/contactUs.html")


books = [
    {"id": 1, 'title': "The Great Gatsby", "no_of_page": 180, "author": "F. Scott Fitzgerald", "price": 800, "image": "leather-book-preview.png"},
    {"id": 2, 'title': "To Kill a Mockingbird", "no_of_page": 281, "author": "Harper Lee", "price": 1200, "image": "leather-book-preview.png"},
    {"id": 3, 'title': "1984", "no_of_page": 328, "author": "George Orwell", "price": 950, "image": "leather-book-preview.png"},
    {"id": 4, 'title': "The Catcher in the Rye", "no_of_page": 277, "author": "J.D. Salinger", "price": 700, "image": "leather-book-preview.png"},
]


def booksHome(request):
    return render(request, "books/home.html",context = {"name": "noha", "books": books})




def bookProfile(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, "books/details.html", context={
            "book": book
        })

    return HttpResponse("book not found")


def booksIndex(request):
    books  = Book.objects.all()
    print(books)
    return render(request, "crud/index.html",context={"books": books})



def bookShow(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "crud/details.html", context={"book": book})


def bookDelete(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    url = reverse("booksIndex")
    return redirect(url)



def bookCreate(request):
    print(request)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        book = Book(title=request.POST["title"], author=request.POST["author"]
                    ,no_of_page=request.POST["no_of_page"],price=request.POST["price"], image=image)
        book.save()
        return redirect(book.showURL)

    # post request

    # get request
    return  render(request, 'crud/create.html')


def updateBook(request,id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = book.image
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.price = request.POST["price"]
        book.numberOfPages = request.POST["numberofpages"]
        book.image = image
        book.save()
        return redirect(book.showURL)
    # book = get_object_or_404(Book, pk=id)
    return render(request, "crud/updateBook.html", {"book":book})



def book_create_forms(request):
    form = bookForm()
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            book = Book(title=form.cleaned_data["title"], author=form.cleaned_data["author"]
                ,no_of_page=form.cleaned_data["no_of_page"],price=form.cleaned_data["price"], image=image)
            book.save()
            return redirect(book.showURL)
    return render(request,"forms/create.html",context={"form":form})




def book_model_form(request):
    form=bookModelform()
    if request.method=="POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        form = bookModelform(request.POST,request.FILES)
        if form.is_valid():
            book=form.save()
            return redirect(book.showURL)
    return render(request,"forms/create.html",context={"form":form})

def edit_model_form(request,id):
    book=Book.get_book_by_id(id)
    form =bookModelform(instance=book)
    if request.method=="POST":
        form = bookModelform(request.POST,request.FILES,instance=book)
        if form.is_valid():
            book.save()
            return redirect(book.showURL)
        
    return render(request,"forms/create.html",context={"form":form})
    