from django import forms

class LoginForms(forms.Form):
   nome_login = forms.CharField(
      label="Nome de Login",
      required=True,
      max_length=100,
      widget=forms.TextInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite seu login'})
    ) 

   senha = forms.CharField(
      label="Senha",
      required=True,
      max_length=70,
      min_length=3,
      widget=forms.PasswordInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite sua senha'})
   ) 

class CadastroForms(forms.Form)   :
   nome_cadastro = forms.CharField(
      label="Nome",
      required=True,
      max_length=100,
      widget=forms.TextInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite seu primeiro nome'})
    )   

   sobrenome_cadastro = forms.CharField(
      label="Sobrenome",
      required=True,
      max_length=100,
      widget=forms.TextInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite seu sobrenome'})
    ) 
   
   email = forms.EmailField(
      label="E-mail",
      required=True,
      max_length=100,
      widget=forms.EmailInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite seu E-mail'})
   )

   nome_login = forms.CharField(
      label="Nome de Login",
      required=True,
      max_length=100,
      widget=forms.TextInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite seu login'})
    ) 

   senha_1 = forms.CharField(
      label="Senha",
      required=True,
      max_length=70,
      min_length=3,
      widget=forms.PasswordInput(attrs={
         'class': 'form-control', 
         'placeholder':'Digite sua senha'})
   ) 

   senha_2 = forms.CharField(
      label="Senha",
      required=True,
      max_length=70,
      min_length=3,
      widget=forms.PasswordInput(attrs={
         'class': 'form-control', 
         'placeholder':'Repita a sua senha'})
   )  