from django.shortcuts import render
from produtos.models import Produtos
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from produtos.models import Produtos
from django.shortcuts import get_object_or_404
from produtos.models import DeducaoHistorico
import json



@login_required
def home(request):
    dados = Produtos.objects.all()
    return render(
        request,
        'home.html',
        {'dados':dados},        
                  )

def deduzir_valor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            dados = data.get('dados', [])

            for item in dados:
                produto_id = item.get('id')
                quantidade_deduzir = item.get('quantidade')

                produto = get_object_or_404(Produtos, id=produto_id)

                if quantidade_deduzir <= produto.quantidade:
                    produto.quantidade -= quantidade_deduzir
                    produto.save()

                    
                    DeducaoHistorico.objects.create(
                        usuario=request.user, 
                        produto=produto,
                        quantidade_deduzida=quantidade_deduzir
                    )
                else:
                    return JsonResponse({'mensagem': 'Quantidade a deduzir é maior que a quantidade disponível.'}, status=400)

            return JsonResponse({'mensagem': 'Valores deduzidos com sucesso.'})
        except Exception as e:
            return JsonResponse({'mensagem': f'Erro ao deduzir valores: {str(e)}'}, status=500)

    return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)
