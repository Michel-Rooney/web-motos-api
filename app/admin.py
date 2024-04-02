from django.contrib import admin

from .models import Carro
from .models import UserBase

admin.site.register(UserBase)
admin.site.register(Carro)
