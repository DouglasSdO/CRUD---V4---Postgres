from django.db import models

#Dados cadastrais dos clintes / ao editar ou incluir deve-se realizar a migração para o banco.

class Cadastro(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    telefone = models.DecimalField(max_digits=10, decimal_places=1)
    cpf = models.DecimalField(max_digits=10, decimal_places=1)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)