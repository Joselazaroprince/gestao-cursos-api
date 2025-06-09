Descrição da API – Sistema de Gestão Acadêmica
📌 Objetivo
A API foi desenvolvida para gerenciar dados acadêmicos de forma simples e eficiente, permitindo o registro, consulta e atualização de informações relacionadas a cursos, módulos e inscrições de estudantes. É ideal para uso em instituições de ensino, centros de formação ou sistemas internos de matrícula.

⚙️ Tecnologias Utilizadas
Framework: Django + Django REST Framework (DRF)

Linguagem: Python

Banco de Dados: SQLite (padrão do Django)

Padrão de Projeto: RESTful

📂 Principais Recursos da API
🔹 1. Autenticação de Usuário
Endpoint de login para administradores via /login/

Proteção dos endpoints principais com autenticação

Geração de tokens JWT (dependendo da configuração)

🔹 2. Cursos
GET /cursos/: Lista todos os cursos

POST /cursos/: Cria um novo curso

PUT /cursos/{id}/: Atualiza um curso existente

DELETE /cursos/{id}/: Remove um curso

🔹 3. Módulos
GET /modulos/: Lista os módulos disponíveis

POST /modulos/: Adiciona um novo módulo vinculado a um curso

PUT /modulos/{id}/: Atualiza informações do módulo

DELETE /modulos/{id}/: Remove um módulo

🔹 4. Inscrições
GET /inscricoes/: Lista as inscrições realizadas

POST /inscricoes/: Cadastra uma nova inscrição com nome de estudante e curso

PUT /inscricoes/{id}/: Atualiza dados da inscrição

DELETE /inscricoes/{id}/: Exclui uma inscrição

🛡️ Segurança
Os endpoints principais estão protegidos contra acessos não autorizados.

O sistema de login serve como camada de autenticação básica para evitar uso indevido.

💻 Frontend Integrado
Interface construída com HTML, CSS e Bootstrap para consumo da API.

Telas separadas para:

Login

Gestão de Cursos

Gestão de Módulos

Inscrição de Estudantes



Deve se ter em consciência que ao se fazer login, o user é admin e a password é 1234
