from django.db import models

# Create your models here.

class Clientes(models.Model):
    cpf = models.CharField(primary_key = True,
                           max_length = 11,
                           help_text = "Informe o seu CPF")
    
    nome = models.CharField(max_length = 100,
                            help_text = "Informe o seu nome")
    
    endereco = models.CharField(max_length = 100,
                                help_text = "Insira o seu endereço")
    
    telefone = models.CharField(max_length = 11,
                                help_text = "Insira o seu número de telefone")
    
    uf = models.CharField(max_length = 2,
                          help_text = "Insira o estado de domicílio")
    
    cidade = models.CharField(max_length = 50,
                              help_text = "Insira a cidade")
    
    genero = models.CharField(max_length = 1,
                              help_text = "Insira o gênero")
    
    contato = models.CharField(max_length = 100,
                               help_text = "Insira a forma de contato")
    
    email = models.CharField(max_length = 100,
                             help_text = "Insira o email para contato")
    
    senha = models.CharField(max_length = 256,
                             help_text = "Insira a senha")