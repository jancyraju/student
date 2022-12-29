from django.contrib import admin

# Register your models here.
from .models import Course,Contact

admin.site.register(Course)

class customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,customerdetails)