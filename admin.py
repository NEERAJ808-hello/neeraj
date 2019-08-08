from django.contrib import admin
from .models import users, Notes, MyNotes
# Register your models here.

admin.site.register(users)
admin.site.register(Notes)
admin.site.register(MyNotes)