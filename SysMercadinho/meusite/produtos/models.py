from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    
    
class Produtos(models.Model):
    nome = models.CharField(
        max_length=100
        )
    
    preco = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        )
    quantidade = models.IntegerField(
        default=0,
    )
    categoria =models.ForeignKey(
        Categoria, 
        on_delete=models.DO_NOTHING,
        )
    
    def __str__(self):
        return self.nome
    