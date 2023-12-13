from django.shortcuts import render,redirect
from django.http import HttpResponse
from produtos.models import Produtos
# Create your views here.


def home(request):
    dados = Produtos.objects.all()
    return render(
        request,
        'home.html',
        {'dados':dados},        
                  )
    
'''def deduzir_valor(request, produto_id, quantidade_deduzir):
    produto = Produtos.objects.get(
        pk=produto_id
        )

    # Deduzir a quantidade do produto
    produto.quantidade -= quantidade_deduzir
    produto.save()

    return redirect('/')'''

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from produtos.models import Produtos
from django.shortcuts import get_object_or_404

@csrf_exempt
def deduzir_valor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            dados = data.get('dados', [])

            for item in dados:
                produto_id = item.get('id')
                quantidade_deduzir = item.get('quantidade')

                # Utilize get_object_or_404 para evitar o erro "Produtos matching query does not exist"
                produto = get_object_or_404(Produtos, id=produto_id)
                
                # Verifica se a quantidade a deduzir não ultrapassa a quantidade atual
                if quantidade_deduzir <= produto.quantidade:
                    produto.quantidade -= quantidade_deduzir
                    produto.save()
                else:
                    return JsonResponse({'mensagem': 'Quantidade a deduzir é maior que a quantidade disponível.'}, status=400)

            return JsonResponse({'mensagem': 'Valores deduzidos com sucesso.'})
        except Exception as e:
            return JsonResponse({'mensagem': f'Erro ao deduzir valores: {str(e)}'}, status=500)

    return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)
