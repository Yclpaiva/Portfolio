"""from django.urls import path
from . import views
from .views import deduzir_valor

urlpatterns = [
    
    path(
        '',
        views.home,
        name='home',
        ),
    
    path('/deduzir_valor/<int:produto_id>/<int:quantidade_deduzir>/',
         views.deduzir_valor,
         name='deduzir_valor',
         ),
    
]


urlpatterns = [
    # Suas outras rotas aqui...
    path('deduzir_valor/', deduzir_valor, name='deduzir_valor'),
]


"""

# urls.py
from django.urls import path
from . import views
from .views import deduzir_valor

urlpatterns = [
    # Suas outras rotas aqui...
    path(
            '',
            views.home,
            name='home',
            ),
    
    path('deduzir_valor/', deduzir_valor, name='deduzir_valor'),
]
