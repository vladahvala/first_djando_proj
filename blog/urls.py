from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.blog_main), #це все відповідає шляху domen.com/blog/ (в r'' - порожньо)
    path('<slug>/', views.slug_process), #з <> дані передаються в views.blog_main
]
#r - вказує, що стрічка є регулярним виразом
#re_path - шлях теж стає регулярним
#'^a' - точний початок стрічки в адресі, введеній користувачем
#r'([0-9]{4})' - означає, що запускатииметься сайт тільк після введення 4 цифр у кінці адреси
