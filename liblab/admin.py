from django.contrib import admin
from .models import User
from .models import Libuser
from .models import Libitem

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email', 'gender')
    list_display_links = ('f_name', 'l_name')
    search_fields = ('f_name', 'l_name')

admin.site.register(Libuser)
admin.site.register(Libitem)
admin.site.register(User, UserAdmin)
