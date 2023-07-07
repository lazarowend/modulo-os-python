import os

caminho = os.path.join('home/users', 'desktop', 'arquivo.txt')
print(caminho)
print(os.path.dirname(caminho))


caminho, arquivo = os.path.split(caminho)
print(caminho, arquivo)

arquivo, extencao = os.path.splitext(arquivo)
print(arquivo, extencao)

print(os.path.exists(caminho))
print(os.path.exists('/home/lazaro/Documentos/PYTHON/modulos'))

caminho_atual = os.path.abspath('.')
print(caminho_atual)

base = os.path.basename(caminho_atual)
print(base)
