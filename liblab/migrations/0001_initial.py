# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 14:58
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('itemtype', models.CharField(choices=[('Book', 'Book'), ('DVD', 'DVD'), ('Other', 'Other')], default='Book', max_length=6)),
                ('checked_out', models.BooleanField(default=False)),
                ('duedate', models.DateField(default=None, null=True)),
                ('last_chkout', models.DateField(default=None, null=True)),
                ('date_acquired', models.DateField(default=django.utils.timezone.now)),
                ('pubyr', models.IntegerField(verbose_name='Publish Year')),
                ('num_chkout', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Libuser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(default='Windsor', max_length=20)),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec')], default='ON', max_length=2)),
                ('phone', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='liblab.Libitem')),
                ('author', models.CharField(max_length=100)),
                ('category', models.IntegerField(choices=[(1, 'Fiction'), (2, 'Biography'), (3, 'Self Help'), (4, 'Education'), (5, 'Children'), (6, 'Teen'), (7, 'Other')], default=1)),
            ],
            bases=('liblab.libitem',),
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='liblab.Libitem')),
                ('maker', models.CharField(blank=True, max_length=100)),
                ('duration', models.IntegerField(blank=True)),
                ('rating', models.IntegerField(choices=[(1, 'G'), (2, 'PG'), (3, 'PG-13'), (4, '14A'), (5, 'R'), (6, 'NR')], default=1)),
            ],
            bases=('liblab.libitem',),
        ),
        migrations.AddField(
            model_name='libitem',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='liblab.Libuser'),
        ),
    ]
