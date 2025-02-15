from django.db import models

class Pacientes(models.Model):
    queixa_choices = (
        ('TDAH', 'TDAH'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('TAG', 'Transtorno de ansiedade generalizada')
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    queixa = models.CharField(max_length=4, choices=queixa_choices, default='TDAH')
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
