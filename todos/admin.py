from django.contrib import admin

# Register your models here.
from .models import Todos,Priority

admin.site.register(Todos)
admin.site.register(Priority)
