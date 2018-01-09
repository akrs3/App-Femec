from django.contrib import admin
from .models import Umec, BoardFemec, BoardUmec



class BoardFemecAdmin(admin.ModelAdmin):
    def dataNasc(self, obj):
        return obj.date.strftime('%d/%m')
    list_display = ('name', 'office_verbose','dataNasc','fone','email','address',)
    


class BoardUmecAdmin(admin.ModelAdmin):
    def dataNasc(self, obj):
        return obj.date.strftime('%d/%m')
    list_display = ('name', 'office_verbose','dataNasc','fone','email','address',)
    


# Register your models here.

admin.site.register(BoardFemec, BoardFemecAdmin)
admin.site.register(BoardUmec, BoardUmecAdmin)
admin.site.register(Umec)