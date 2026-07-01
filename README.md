# Pé Confortável Ltda.

Projeto desenvolvido para a Atividade Avaliativa da Unidade Curricular 3 (UC3), utilizando o framework Django.

## Descrição

O sistema simula parte da informatização da rede de lojas **Pé Confortável Ltda.**, permitindo o gerenciamento de produtos e fabricantes por meio de uma aplicação web.

As funcionalidades implementadas seguem os requisitos da atividade proposta pelo Senac.

## Funcionalidades

### Página Inicial
- Apresentação da empresa
- Menu de navegação

### Produtos
- Cadastro de produtos
- Listagem de produtos

### Fabricantes
- Cadastro de fabricantes
- Listagem de fabricantes

### Administração
- Painel administrativo do Django
- Cadastro e gerenciamento dos registros

## Tecnologias Utilizadas

- Python 3
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite3

## Estrutura do Projeto

```
pe_confortavel/
│
├── loja/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── loja/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── pe_confortavel/
├── db.sqlite3
├── manage.py
└── README.md
```

## Como executar o projeto

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install django
```

Ou utilizando:

```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações

```bash
python manage.py migrate
```

### 5. Executar o servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

## Painel Administrativo

Para acessar o painel administrativo:

```
http://127.0.0.1:8000/admin/
```

Utilize o usuário administrador criado através do comando:

```bash
python manage.py createsuperuser
```

## Banco de Dados

O projeto utiliza o banco de dados SQLite, padrão do Django.

## Desenvolvedor

Projeto desenvolvido por **Rômulo Nantes** para a Atividade Avaliativa da Unidade Curricular 3 (UC3).

---

**Instituição:** Senac RJ

**Curso:** Programação em Python

**Framework:** Django