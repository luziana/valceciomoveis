from django.contrib import admin
from .models import Endereco
from .models import Funcionario
from .models import Cargo
from .models import Mercadoria

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Mercadoria)
