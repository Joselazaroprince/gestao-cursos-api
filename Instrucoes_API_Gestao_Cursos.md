# Projeto API RESTful - Gestão de Cursos Online

## 📌 Descrição do Projeto

Este projeto consiste em uma API RESTful desenvolvida com Django e Django REST Framework, conectada a um banco de dados MySQL. O tema é um sistema de gestão de cursos online, com funcionalidades de CRUD completo, relacionamentos entre entidades e preparado para autenticação, documentação e hospedagem.

---

## 📁 Entidades

1. **Curso**: título, descrição.
2. **Módulo**: pertence a um curso, tem título e conteúdo.
3. **Inscrição**: aluno inscrito em um curso, com data.
4. **Usuário**: gerenciado com Django (User).

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- Django 4+
- Django REST Framework
- MySQL
- Gunicorn (para produção)
- Render.com (hospedagem gratuita)

---

## 🚀 Como Executar Localmente

### 1. Clone o repositório

```
git clone <link-do-repositorio-ou-extraia-o-zip>
cd gestao_cursos
```

### 2. Crie um ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```
pip install -r requirements.txt
```

### 4. Configure o banco de dados MySQL

Edite o arquivo `gestao_cursos/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Crie o banco e rode as migrações

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
-------gerar novas migrações com o core-----------
python manage.py makemigrations core
python manage.py migrate core
```

### 6. Rode o servidor local

```
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/api/

---

## 🌐 Como Hospedar Gratuitamente no Render

### 1. Crie uma conta em https://render.com

### 2. Suba seu código para o GitHub

Crie um repositório e envie o projeto para lá.

### 3. Crie um novo serviço no Render

- Clique em "New Web Service"
- Conecte sua conta GitHub
- Escolha o repositório com o projeto
- Configure:

```
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn gestao_cursos.wsgi
```

### 4. Configure variáveis de ambiente

Adicione as variáveis relacionadas ao banco de dados, como:

```
DATABASE_URL=mysql://usuario:senha@host:3306/nome_do_banco
```

### 5. Pronto! A API será hospedada e um link será fornecido.

---

## 📚 Documentação (opcional)

Você pode adicionar Swagger com:

```
pip install drf-yasg
```

E incluir no `urls.py` principal:

```python
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(title="API Cursos", default_version='v1'), public=True)
urlpatterns += [path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger')]
```

Acesse `https://seu-link-deploy/render/swagger/` para visualizar a documentação interativa.

---

## ✅ Checklist para entrega

- [X]  CRUD completo para cada entidade
- [X]  Relacionamentos claros
- [X]  Validações básicas
- [X]  Código organizado em pastas
- [X]  Hospedagem gratuita funcional
- [X]  Repositório GitHub com código
- [X]  README.md com instruções
- [X]  Diagrama de entidades (opcional)
