from django.contrib import admin
from .models import Personal_Information
from .models import School_Information
from .models import Guardian_Information
 
admin.site.register(Personal_Information)
admin.site.register(School_Information)
admin.site.register(Guardian_Information)



# Register your models here.
