from django.contrib import admin
from .models import Book
from .models import Libuser
from .models import Dvd

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email', 'gender')
    list_display_links = ('f_name', 'l_name')
    search_fields = ('f_name', 'l_name')

admin.site.register(Libuser)
admin.site.register(Book)
admin.site.register(Dvd)
