from django import forms
from django.forms import ModelForm

from .models import *

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

class NoticiaForm(ModelForm):

    class Meta:
        model = Noticia
        fields = '__all__'

        widgets = {
            'Tag':forms.CheckboxSelectMultiple(),
        }

class GaleriaForm(ModelForm):
    class Meta:
        model = Galeria
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class TestimonioForm(ModelForm):
    class Meta:
        model = Testimonio
        fields = '__all__'


class NavProductoForm(ModelForm):
    class Meta:
        model = NavProducto
        fields = '__all__'


class InstitucionForm(ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'

class NoticiaMainForm(ModelForm):
    class Meta:
        model = NoticiaInicio
        fields = '__all__'

class CreditoForm(ModelForm):
    class Meta:
        model = Credito
        fields = '__all__'

class NavServicioForm(ModelForm):
    class Meta:
        model = NavServicio
        fields = '__all__'