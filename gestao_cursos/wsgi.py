import os
import sys
from django.core.wsgi import get_wsgi_application

# Adicione o caminho do seu projeto ao Python path
path = '/home/joselazaroprince/gestao-cursos-api'  # Ajuste para seu caminho real
if path not in sys.path:
    sys.path.append(path)

# Defina as variáveis de ambiente necessárias
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_cursos.settings')
os.environ.setdefault('ENVIRONMENT', 'production')  # Garante ambiente de produção

# Configurações específicas para PythonAnywhere
os.environ['PYTHONANYWHERE_DOMAIN'] = 'pythonanywhere.com'

application = get_wsgi_application()

if __name__ == '__main__':
    print("WSGI configurado com sucesso!")
    print(f"PYTHONPATH: {sys.path}")
    print(f"ENV: {os.environ.get('DJANGO_SETTINGS_MODULE')}")