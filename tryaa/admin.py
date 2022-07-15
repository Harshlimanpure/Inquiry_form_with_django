from django.contrib import admin
from .models import MForm
# Register your models here.

@admin.register(MForm)
class RegAdmin(admin.ModelAdmin):
    list_dispplay= ['id','name','email','password']
