# Generated by Django 4.0.4 on 2022-07-15 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryaa', '0003_form_father_name_form_mother_name_form_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Father_name',
            new_name='father_name',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Mother_name',
            new_name='mother_name',
        ),
    ]
