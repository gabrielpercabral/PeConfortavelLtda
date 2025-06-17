from django import forms

class ClientesForm(forms.Form):
    cpf = forms.CharField(max_length = 11,
                          help_text = "Informe o seu CPF")
    
    nome = forms.CharField(max_length = 100,
                           help_text = "Informe o seu nome")
    
    endereco = forms.CharField(max_length = 100,
                               help_text = "Insira o seu endereço")
    
    telefone = forms.CharField(max_length = 11,
                               help_text = "Insira o seu número de telefone")
    
    uf = forms.CharField(max_length = 2,
                         help_text = "Insira o estado de domicílio")
    
    cidade = forms.CharField(max_length = 50,
                             help_text = "Insira a cidade")
    
    genero = forms.CharField(max_length = 1,
                             help_text = "Insira o gênero")
    
    contato = forms.CharField(max_length = 100,
                              help_text = "Insira a forma de contato")
    
    email = forms.CharField(max_length = 100,
                            help_text = "Insira o email para contato")
    
    senha = forms.CharField(max_length = 256,
                            help_text = "Insira a senha")