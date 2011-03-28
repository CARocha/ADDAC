from django.contrib import admin
from addac.noticias.models import Noticia, CategoriaNoticia
from django.contrib.contenttypes import generic
from addac.extras.models import Adjunto #importando el modelo de adjuntos genericos

class CategoriaNoticiaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    list_per_page = 12

class AdjuntoInline(generic.GenericStackedInline):
    model = Adjunto
    extra = 1
    max_num = 3

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','tipo','categoria']
    list_filter = ['categoria','tipo']
    search_fields = ['titulo']
    inlines = [AdjuntoInline,]
    save_on_top = True
    date_hierarchy = 'fecha'
    list_per_page = 12

    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]

#class ComentarioAdmin(admin.ModelAdmin):
#    list_display = ['nombre', 'fecha','estado','noticia' ]
#    list_filter = ['estado']
#    search_fields = ['nombre']
#    save_on_top = True
#    date_hierarchy = 'fecha'
#    actions = ['publicar','nopublicar']

#    def publicar(self, request, queryset):
#        queryset.update(estado=True)
#    publicar.short_description = "Marcar los comentarios como publicados"

#    def nopublicar(self, request, queryset):
#        queryset.update(estado=False)
#    nopublicar.short_description = "Marcar los comentarios como No Publicados"

admin.site.register(CategoriaNoticia, CategoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
#admin.site.register(Comentario, ComentarioAdmin)
