import datetime
from django.contrib import admin
from .models import Libitem
from .models import Book
from .models import Libuser
from .models import Dvd


class BookInline(admin.StackedInline):
    model = Book  # This shows all fields of Book.
    fields = [('title', 'author', 'pubyr'), 'duedate',]   #  Customizes to show only certain fields
    extra = 0

def renew(modeladmin, request, queryset):
    update_count = 0
    update_msg = ""
    for obj in queryset:
        if obj.checked_out == True:
            update_count += 1
            queryset.filter(title=obj.title).filter(user=obj.user)\
                .update(duedate=obj.duedate+datetime.timedelta(days=21))

    if update_count == 1:
        update_msg = "1 record was"
    elif update_count > 1:
        update_msg = "%s records were" % update_count
    modeladmin.message_user(request, "%s successfully renewed!" % update_msg)

renew.short_description = "Renew selected item"

class DvdInline(admin.TabularInline):
    model = Dvd  # This shows all fields of Book.
    fields = [('title', 'maker', 'duration', 'rating','pubyr'), 'duedate']  # Customizes to show only certain fields
    extra = 0


class LibuserAdmin(admin.ModelAdmin):
    fields = [('username'), ('first_name', 'last_name')]
    inlines = [BookInline, DvdInline]


class BookAdmin(admin.ModelAdmin):
    fields = [('title', 'author', 'pubyr'), ('checked_out', 'user', 'duedate'),'category']
    list_display = ('title', 'borrower', Libitem.overdue)
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user     #Returns the user who has borrowed this book
        else:
            return ''


class DvdAdmin(admin.ModelAdmin):
    fields = [('title', 'maker', 'pubyr'), ('checked_out', 'user', 'duedate'),'rating']
    list_display = ('title', 'borrower', Libitem.overdue)

    def borrower(self, obj=None):
        if obj.checked_out == True:
            return obj.user     #Returns the user who has borrowed this book
        else:
            return ''

admin.site.register(Libuser, LibuserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Dvd, DvdAdmin)
