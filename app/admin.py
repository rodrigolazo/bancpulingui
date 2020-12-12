from django.contrib import admin

# Register your models here.
from.models import *

from import_export.admin import ImportExportModelAdmin

class BancoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        model = Post, Tag, Info, Noticia, Galeria, Producto, Testimonio, NavProducto, NavServicio, Institucion, NoticiaInicio, Credito

admin.site.register(Post, BancoAdmin)
admin.site.register(Tag, BancoAdmin)
admin.site.register(Info, BancoAdmin)
admin.site.register(Noticia, BancoAdmin)
admin.site.register(Galeria, BancoAdmin)
admin.site.register(Producto, BancoAdmin)
admin.site.register(Testimonio, BancoAdmin)
admin.site.register(NavProducto, BancoAdmin)
admin.site.register(NavServicio, BancoAdmin)
admin.site.register(Institucion, BancoAdmin)
admin.site.register(NoticiaInicio, BancoAdmin)
admin.site.register(Credito, BancoAdmin)
