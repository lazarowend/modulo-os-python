import os
from itertools import count
# caminho = "/home/lazaro/Documentos/PYTHON/modulos/modulo_os"

counter = count()

caminho = os.path.join('/home', 'lazaro', 'Documentos', 'PYTHON', 'modulos', 'modulo_os', 'exemplo')

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(f'{the_counter} -- {root}')

    for _dir in dirs:
        print(f'    {the_counter} -- {_dir}')

    for _file in files:
        caminho_completo = os.path.join(root, _file)
        print(f'    {the_counter} -- {_file} -- {caminho_completo}')
        # os.unlink(caminho)
        # apaga a pasta sem chances de restaurar