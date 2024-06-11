# dio-twitter-py


## Sobre o Projeto
Este projeto foi desenvolvido como parte do curso Python Developer na DIO, durante o webinar "Consumindo a API do Twitter com Python" ministrado pelo professor Guilherme Carvalho.

## Tecnologias 📚
Python 3.8.x
FastAPI
MongoDB

## Requisitos ✋
Docker
Docker Compose
Poetry

## Instalação 💽
Instale o Docker e Docker Compose no seu computador.
Instale o Poetry para gerenciar as dependências do projeto.
Clone o repositório:

```sh
git clone https://github.com/seu-usuario/dio-twitter-py.git
cd dio-twitter-py
```

Instale as dependências:

```sh
poetry install
```

## Rodando a aplicação 🛸
Inicie o ambiente virtual e rode a aplicação:

```sh
poetry shell
python main.py
```

Acesse o Swagger UI para listar todos os endpoints.

Use Ctrl+C para finalizar o processo servidor.

## Rodando os testes 🧪
Para rodar os testes, execute:

```sh
poetry shell
pytest
```

## Docker 🐳
Para rodar a aplicação utilizando Docker e Docker Compose, siga os seguintes passos:

Construa a imagem Docker:
```sh
docker-compose build
```
Inicie os containers:
```sh
docker-compose up
```
A aplicação estará disponível em http://localhost:8000.