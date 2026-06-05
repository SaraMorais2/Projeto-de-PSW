from django.contrib import admin
from django.urls import path, include
from estudantes import views

app_name = "estudanes"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudantes/', include('estudantes.urls')), 
    path('cursos/', include('cursos.urls')),
    path('notas/', include('desempenho.urls'))
]
