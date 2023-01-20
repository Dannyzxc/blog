from django import forms
from .models import *

# cats = [('tech','tech'),('fashion','fashion'),('makeup','makeup')]

cats = Catergory.objects.all().values_list('name','name')


class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ('title','categories','title_tag','author','content')
 
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'categories':forms.Select(choices = cats ,attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }


class updateform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

