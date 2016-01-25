# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from passwords.fields import PasswordField

from .models import CustomUser, Endereco, Funcionario


class UserCreationForm(forms.ModelForm):
    password_help_text = u"A senha deve conter no mínimo 6 caracteres, \
                           sendo 1 letra maiúscula, 1 letra minúscula e 2 números."
    password1 = PasswordField(label='senha', help_text=password_help_text)
    password2 = PasswordField(label='confirmar senha', help_text=password_help_text)

    class Meta:
        model = CustomUser
        fields = ('cpf',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(u'As senhas não são iguais.')
        return password2

    def save(self, commit=True):
        usuario = super(UserCreationForm, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class UserChangeFormAdmin(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Senha",
                                         help_text="<a href=\"password/\">Mudar a senha</a>.")

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

