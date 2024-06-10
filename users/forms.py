from django import forms
from django.views.generic import UpdateView

from users.models import Vacancy, Person


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name','style','qualification','job_duties','opportunities']

class VacancyUpdateForm(UpdateView):
    model = Vacancy
    fields = ['name','style','qualification','job_duties','opportunities']



class UserCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username','phone_number','first_name','last_name', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email')
