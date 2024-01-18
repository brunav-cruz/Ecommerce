from django.contrib import admin
from .models import Produto
from .models import Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)