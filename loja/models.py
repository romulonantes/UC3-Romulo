from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    CORES = [
        ('azul', 'Azul'), ('vermelho', 'Vermelho'), ('verde', 'Verde'),
        ('amarelo', 'Amarelo'), ('branco', 'Branco'), ('preto', 'Preto'), ('marrom', 'Marrom')
    ]

    nome = models.CharField(max_length=70)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    cor = models.CharField(max_length=20, choices=CORES)
    data_fabricacao = models.DateField()
    imagem = models.CharField(max_length=25, help_text='Nome da imagem do produto')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
