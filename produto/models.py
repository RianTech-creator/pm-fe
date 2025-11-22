from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    estoque = models.PositiveIntegerField(default=0)
    foto = models.URLField(max_length=200, blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
