from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import View, UpdateView

from users.forms import VacancyForm, VacancyUpdateForm, UserCreateForm
from users.models import Vacancy
from djangoProject1.kadr_permission import OnlyLoggedKadr, OnlyLoggedManager

class VacancyView(View):
    def get(self, request):

        vacancies = Vacancy.objects.filter(active=True).order_by('-created_at')
        user = request.user
        if user.is_authenticated and user.is_kadr:
            vacancies = Vacancy.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'vacancies': vacancies})

class VacancyDetailView(View):
    def get(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        remaining_days = (vacancy.end_at - timezone.now().date()).days
        return render(request, 'vacancy/detail.html', {'vacancy': vacancy, 'remaining_days': remaining_days})
        # return render(request, 'vacancy/detail.html', {'vacancy': vacancy})


class VacancyAddView(OnlyLoggedKadr, View):
    def get(self, request):
        vacancy_form = VacancyForm()

        return render(request, 'vacancy/add_vacancy.html', {'form': vacancy_form})

    def post(self, request):
        vacancy_form = VacancyForm(request.POST)

        if vacancy_form.is_valid():
            vacancy = vacancy_form.save(commit=False)
            vacancy.save()
            messages.success(request, 'Vacancy added successfully')

            return redirect('users:home')

        else:
            messages.error(request, 'Something went wrong')
            return redirect('users:home')

class VacancyChangeActiveView(OnlyLoggedKadr,OnlyLoggedManager, View):
    def get(self, request, pk):
        vacancy = Vacancy.objects.get(pk=pk)
        if vacancy.active:
            vacancy.active = False
        else:
            vacancy.active = True
        vacancy.save()

        return redirect('users:home')

class VacancyUpdateView(OnlyLoggedKadr, OnlyLoggedManager, UpdateView):
    model = Vacancy
    fields = ('name','style','qualification','job_duties','opportunities')
    template_name = 'vacancy/update_vacancy.html'
    success_url = reverse_lazy('users:home')

class LoginView(View):
    def get(self, request):
        # login_form = UserLoginForm()
        login_form = AuthenticationForm()

        return render(request=request, template_name='registration/login.html',context= {'form' : login_form})

    def post(self, request):
        # print(request.POST['username'], request.POST['password'])

        # login_form = UserLoginForm(data=request.POST)

        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')

            return redirect('books:list')
        else:
            return render(request=request, template_name='registration/login.html',context= {'form' : login_form})



class RegisterView(View):
    def get(self, request):
        create_user = UserCreateForm()

        context = {
            'form':create_user
        }
        return render(request=request, template_name='registration/register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request=request, template_name='registration/register.html', context=context)



