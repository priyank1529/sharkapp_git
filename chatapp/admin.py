from django.contrib import admin

# Register your models here.
from .models import Sharks,Pitcher,Pitcher_company
admin.site.register(Sharks)
admin.site.register(Pitcher)
admin.site.register(Pitcher_company)
