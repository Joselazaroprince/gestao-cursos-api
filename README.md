# 🎓 Gestão de Cursos API

Este é um projeto de API RESTful para gerenciamento de cursos, módulos e inscrições, desenvolvido em **Django** com **Django REST Framework**. Ele permite o registro de cursos, organização por módulos e controle de inscrições de alunos, com autenticação via JWT.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MySQL](https://www.mysql.com/) (local) / [PostgreSQL](https://www.postgresql.org/) (hospedado)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Railway](https://railway.app/) (Deploy)
- [Gunicorn](https://gunicorn.org/) (produção)

---

## 📦 Funcionalidades

- ✅ Cadastro e listagem de **Cursos**
- ✅ Organização de cursos em **Módulos**
- ✅ Inscrição de **Alunos** em cursos
- ✅ Autenticação segura via **JWT**
- ✅ API protegida para usuários autenticados
- ✅ Projeto pronto para produção (Gunicorn, Railway)


---


## 📂 Estrutura dos Endpoints

### 📚 Cursos

| Método | Endpoint           | Descrição                    |
|--------|--------------------|------------------------------|
| GET    | /api/cursos/       | Lista todos os cursos        |
| POST   | /api/cursos/       | Cria um novo curso           |
| GET    | /api/cursos/{id}/  | Detalha um curso específico  |
| PUT    | /api/cursos/{id}/  | Atualiza um curso            |
| DELETE | /api/cursos/{id}/  | Deleta um curso              |

### 📦 Módulos

| Método | Endpoint            | Descrição                    |
|--------|---------------------|------------------------------|
| GET    | /api/modulos/       | Lista todos os módulos       |
| POST   | /api/modulos/       | Cria um novo módulo          |
| GET    | /api/modulos/{id}/  | Detalha um módulo específico |
| PUT    | /api/modulos/{id}/  | Atualiza um módulo           |
| DELETE | /api/modulos/{id}/  | Deleta um módulo             |

### 📝 Inscrições

| Método | Endpoint               | Descrição                          |
|--------|------------------------|------------------------------------|
| GET    | /api/inscricoes/       | Lista todas as inscrições          |
| POST   | /api/inscricoes/       | Realiza nova inscrição             |

---

## 🔐 Autenticação

A autenticação é feita via JWT:

- `POST /api/token/`: Obter token
- `POST /api/token/refresh/`: Atualizar token

---

## 🛠 Como Rodar Localmente

```bash
# Clonar repositório
git clone https://github.com/Joselazaroprince/gestao-cursos-api.git
cd gestao-cursos-api

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar banco de dados (MySQL ou PostgreSQL)
# Atualizar gestao_cursos/settings.py com as credenciais

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Rodar servidor local
python manage.py runserver
