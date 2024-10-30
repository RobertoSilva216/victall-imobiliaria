# Projeto Imobiliária

Este é um projeto Django para a administração de uma imobiliária, permitindo o cadastro de clientes e imóveis, e a gestão de locações.

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Django (instalado como parte do processo abaixo)

## Instalação

**Clone o repositório:**

```bash
   git clone https://github.com/RobertoSilva216/victall-imobiliaria.git
   cd victall-imobiliaria
```

**Crie um ambiente virtual (opcional, mas recomendado):**

```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux ou Mac
   venv\Scripts\activate  # Para Windows
```
**Instale o Django:**

```bash
   pip install django
```

## Configurar banco de dados

**Realize as migrações:**

```bash
   python manage.py makemigrations
   python manage.py migrate
```

## Rodando o Servidor

**Inicie o servidor de desenvolvimento:**

```bash
   python manage.py runserver
```

## Rodando o Servidor
**Acesse a aplicação**

- Abra um navegador e vá até http://127.0.0.1:8000/.