import datetime
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User

class Libuser(User):
    PROVINCE_CHOICES = (
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Libitem(models.Model):
    TYPE_CHOICES = (
        ('Book', 'Book'),
        ('DVD', 'DVD'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Book')
    checked_out = models.BooleanField(default=False)
    user = models.ForeignKey(Libuser, default=None, null=True)
    duedate = models.DateField(default=None, null=True)
    last_chkout = models.DateField(default=None, null=True)
    date_acquired = models.DateField(default=timezone.now)
    pubyr = models.IntegerField("Publish Year")
    num_chkout = models.IntegerField(default=0)

    def overdue(self):
        if self.checked_out == True:
            if timezone.now().date() < self.duedate:
                return "Yes"
            else:
                return "No"


class Book(Libitem):
    CATEGORY_CHOICES = (
        (1, 'Fiction'),
        (2, 'Biography'),
        (3, 'Self Help'),
        (4, 'Education'),
        (5, 'Children'),
        (6, 'Teen'),
        (7, 'Other'),
    )
    author = models.CharField(max_length=100)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)

    def __init__(self, *args, **kwargs):
        self._meta.get_field('itemtype').default = 'Book'
        super(Book, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.title + ' by ' + self.author


class Dvd(Libitem):
    RATING_CHOICES = (
        (1, 'G'),
        (2, 'PG'),
        (3, 'PG-13'),
        (4, '14A'),
        (5, 'R'),
        (6, 'NR'),
    )
    maker = models.CharField(max_length=100, blank=True)
    duration = models.IntegerField(blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __init__(self, *args, **kwargs):
        self._meta.get_field('itemtype').default = 'DVD'
        super(Dvd, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.title + ' by ' + self.maker