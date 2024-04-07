from django import  forms
from books.models import Book
class bookForm(forms.Form):
    pass
    title = forms.CharField(max_length=100,label="Book Title",required=True)
    author = forms.CharField(max_length=100,label="Book Author",required=True)
    no_of_page = forms.IntegerField(label="No of Pages",required=True)
    price = forms.IntegerField(label="Book Price",required=True)
    image = forms.ImageField(required=False, label='Image')

    def clean_title(self):
        title=self.cleaned_data['title']
        title_found= Book.objects.filter(title=title).exists()
        if title_found:
            raise forms.ValidationError("title already exist , pls choose another")
        return title
    


class bookModelform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author)<2:
            raise forms.ValidationError('Name length must be greater than 2 chars')
        return author