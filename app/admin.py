from django.contrib import admin

# Register your models here.
from .models import EntryModel

admin.site.register(EntryModel)
