# Generated by Django 2.2.5 on 2019-09-15 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('fname', 'lname'), 'verbose_name': 'Person', 'verbose_name_plural': 'Person'},
        ),
    ]
