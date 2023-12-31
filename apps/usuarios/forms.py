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

   def clean_nome_login(self):
      login = self.cleaned_data.get('nome_login')
      if login:
         login = login.strip()
         if " " in login:
            raise forms.ValidationError('Não pode haver espaços no nome de login.')
         elif not login.islower():
            raise forms.ValidationError('O nome de login deve estar em letras minusculas.')
         else:
            return login
         
   def clean_senha_2(self):
      senha_1 = self.cleaned_data.get('senha_1')   
      senha_2 = self.cleaned_data.get('senha_2') 
      
      if senha_1 and senha_2:
         if senha_1 != senha_2:
            raise forms.ValidationError('As senhas não são iguais')
         else:
            return senha_2
