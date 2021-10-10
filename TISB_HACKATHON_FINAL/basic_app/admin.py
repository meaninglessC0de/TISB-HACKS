from django.contrib import admin

# Register your models here.
from basic_app.models import Doctor, Patient, Comment, Reply
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Comment)
admin.site.register(Reply)
