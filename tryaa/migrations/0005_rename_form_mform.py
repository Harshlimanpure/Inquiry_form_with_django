# Generated by Django 4.0.4 on 2022-07-15 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryaa', '0004_rename_father_name_form_father_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form',
            new_name='MForm',
        ),
    ]