from django.urls import path
from books.views import (aboutUs,contactUs,booksHome,bookProfile,booksIndex,bookShow,
                        bookDelete,bookCreate,updateBook, book_create_forms,book_model_form,edit_model_form)
urlpatterns = [
    path('aboutUs', aboutUs, name='aboutUsPage'),
    path('contactUs', contactUs, name='contactUsPage'),
    path('booksHome', booksHome, name='HomePage'),
    path('bookProfile/<int:id>', bookProfile, name='bookDetails'),
    path('', booksIndex, name='booksIndex'),
    path('<int:id>', bookShow, name='bookShow'),
    path('<int:id>/delete',bookDelete, name='bookDelete'),
    path('create', bookCreate, name='bookCreate'),
    path('update/<int:id>', updateBook, name='updateBook'),
    path('forms/create',book_create_forms,name='forms.create'),
    path('forms/createByModel',book_model_form,name='forms.create.model'),
    path('forms/<int:id>',edit_model_form,name='forms.edit')
]
