from django import forms


class FabricantesForm(forms.Form):
    nome = forms.CharField(max_length=70, 
                            help_text='Nome do fornecedor')
    
class FabricantesAtualizarForm(forms.Form):
    codigo = forms.IntegerField( 
                           help_text='Codigo do fornecedor')
    nome = forms.CharField(max_length=70, 
                            help_text='Nome do fornecedor')
    