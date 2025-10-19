from django import forms
from store.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('is_active',)
