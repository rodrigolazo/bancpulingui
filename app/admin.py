from django.contrib import admin

# Register your models here.
from.models import *

#from import_export.admin import ImportExportModelAdmin

#class BancoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    class Meta:
#        model = Post, Tag, Info, Noticia, Galeria, Producto, Testimonio, NavProducto, NavServicio, Institucion, NoticiaInicio, Credito

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Info)
admin.site.register(Noticia)
admin.site.register(Galeria)
admin.site.register(Producto)
admin.site.register(Testimonio)
admin.site.register(NavProducto)
admin.site.register(NavServicio)
admin.site.register(Institucion)
admin.site.register(NoticiaInicio)
admin.site.register(Credito)
