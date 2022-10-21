from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            }
        )
    )
    audience = forms.IntegerField(
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Audience',
                'class': 'form-control'
            }
        )
    )
    poster_url = forms.CharField(
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Poster URL',
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Description',
                'class': 'form-control'
            }
        )
    )
    genre = forms.CharField(
        label_suffix='',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },
            choices=(
                ('코미디', '코미디'),
                ('공포', '공포'),
                ('로맨스', '로맨스'),
            )
        )
    )
    score = forms.FloatField(
        label_suffix='',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'min': '0',
                'max': '10',
                'step': '0.5',
                'placeholder': 'Score',
                'class': 'form-control'
            }
        )
    )
    release_date = forms.DateField(
        label_suffix='',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'