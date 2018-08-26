from django.contrib import admin
from .models import Subject, Variation, Entry

# Register your models here.
admin.site.register(Subject)
admin.site.register(Variation)
admin.site.register(Entry)