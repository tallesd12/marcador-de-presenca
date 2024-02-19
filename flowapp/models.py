from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    faixa = models.CharField(max_length=50)
    data = models.DateField()

    def __self__(self):
        return self.nome
