import os
# caminho = "/home/lazaro/Documentos/PYTHON/modulos/modulo_os"

caminho = os.path.join('/home', 'lazaro', 'Documentos', 'PYTHON', 'modulos', 'modulo_os', 'exemplo')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo):
        continue
    
    for img in os.listdir(caminho_completo):
        print('')
        print(img)

