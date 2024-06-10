from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import VacancyView, VacancyAddView, VacancyDetailView, VacancyChangeActiveView, VacancyUpdateView, \
    RegisterView

app_name = 'users'
urlpatterns = [
    path('', VacancyView.as_view(), name='home'),
    path('<int:pk>', VacancyDetailView.as_view(), name='detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('vacancy-add/', VacancyAddView.as_view(), name='add_vacancy'),
    path('vacancy-update/<int:pk>', VacancyUpdateView.as_view(), name='update_vacancy'),
    path('vacancy-delete/<int:pk>', VacancyChangeActiveView.as_view(), name='vacancy_delete'),
]

