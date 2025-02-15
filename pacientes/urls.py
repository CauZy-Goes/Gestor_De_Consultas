from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes, name="pacientes"),
    path('<int:id>', views.paciente_view, name="paciente_view"),
    path('atualizar_paciente/<int:id>', views.atualizar_paciente, name="atualizar_paciente"),
    path('excluir_consulta/<int:id>', views.excluir_consulta, name="excluir_consulta"),
    path('consulta_publica/<int:id>', views.consulta_publica, name="consulta_publica"),
]