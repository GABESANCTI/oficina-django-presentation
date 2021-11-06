from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'conteudo', 'criado_em', 'alterado_em']


admin.site.register(Post, PostAdmin)
