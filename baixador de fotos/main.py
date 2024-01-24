import requests
import os
import time
url_base = 'https://thispersondoesnotexist.com/'
output_directory = 'imagens'
os.makedirs(output_directory, exist_ok=True)

num_imagens = int(input('Digite a quantidade de imagens em "int": '))


for index in range(1, num_imagens + 1):
    time.sleep(0.5)
    url_imagem = f'{url_base}?{index}'
    resposta = requests.get(url_imagem)
    if resposta.status_code == 200:
        conteudo_imagem = resposta.content
        caminho_arquivo = os.path.join(output_directory, f'imagem{index}.jpg')
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(conteudo_imagem)
        print(f'Imagem {index} baixada e salva em {caminho_arquivo}.')
    else:
        print(f'Erro ao baixar a imagem {index}. Código de status: {resposta.status_code}')
