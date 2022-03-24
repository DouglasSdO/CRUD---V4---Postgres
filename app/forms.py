from django.forms import ModelForm
from app.models import Cadastro

   #criação dos campos cadastrais no banco de dados / ao editar ou incluir deve-se realizar a migração para o banco
   #podendo haver problemas de autentificação de chaves.

class CadastroForm(ModelForm):
     class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'cpf', 'cidade', 'estado']