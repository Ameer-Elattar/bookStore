from django.urls import path
from category.views import create_category,category_index,editCategory,categoryDelete

urlpatterns = [
    path('create',create_category,name='createCategory'),
    path('',category_index,name='categoryIndex'),
    path('edit/<int:id>',editCategory,name='editCategory'),
    path('delete/<int:id>',categoryDelete,name='categoryDelete')
]
