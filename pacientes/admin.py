from django.contrib import admin
from .models import Pacientes, Tarefas, Consultas

admin.site.register(Pacientes)
admin.site.register(Tarefas)
admin.site.register(Consultas)