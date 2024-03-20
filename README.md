# API com Sanic e MongoDB

Este projeto consiste em uma API simples desenvolvida em Python, utilizando o framework Sanic para construção do servidor web e o banco de dados MongoDB para armazenamento de dados. A API implementa as operações básicas de CRUD (Create, Read, Update, Delete),permitindo interações com recursos por meio de requisições HTTP.


## 💻 Pré-requisitos

Antes de começar, verifique se você atende aos seguintes requisitos:

- Python na versão 3.10.12 ou superior.
- Sistema Operacional Linux


# Execução do Projeto
Siga estas etapas para configurar e executar o projeto em seu ambiente local

## Passo 1 - Clone ou Baixe o Projeto
Clone o repositório do projeto ou baixe o arquivo zip e extraia-o em seu sistema local.

## Passo 2 - Crie seu Ambiente Virtual
Crie um ambiente virtual utilizando o comando:
```
python3 -m venv venv
```

Ative o ambiente virtual executando:
```
. venv/bin/activate
```

## Passo 3 - Instale as Dependências
Com o ambiente virtual ativo, instale as dependências listadas no arquivo requirements.txt utilizando o seguinte comando:
```
pip install -r requirements.txt
```

## Passo 4 - Execute o Serviço do Banco de Dados
Execute o serviço do banco de dados utilizando o Docker Compose. No terminal, execute o seguinte comando:
```
docker compose up -d
```

## Passo 5 - Inicie o Servidor
Com todas as dependências instaladas e o serviço do banco de dados em execução, inicie o servidor executando o arquivo server.py.
```
python3 server.py
```

## Passo 6 - Teste os Endpoints da API
Utilize uma ferramenta como Postman ou Insomnia para testar os endpoints da API. Abaixo, há um guia detalhado dos endpoints disponíveis.

# Guia dos endpoints da api

## Petshop
* `get/all/petshop/` - Retorna todos os petshops (GET)
* `get/petshop/<id>/` - Busca de petshop por id (GET)
* `create/petshop/` - Criação de petshop (POST)
    * Exemplo de corpo da requisição para criação:
      
      ```
      {
            "nome_petshop": "Cantinho dos Bichinhos",
            "descricao": "O cantinho aconchegante onde os amigos peludos são tratados com carinho e atenção."
      }
      ```
* `update/petshop/<id>/` - Atualização de todo o objeto petshop (PUT)
    * Exemplo de corpo da requisição para atualização completa:
      
      ```
      {
            "nome_petshop": "AmigoFiel Pet Shop"",
            "descricao": "O paraíso dos animais de estimação, onde a felicidade deles é nossa prioridade."
      }
      ```
* `update/petshop/<id>/` - Atualização parcial (PATCH)
    * Exemplo de corpo da requisição para atualização parcial:
      
      ```
      {
             "nome_petshop": "Campina pet"
      }
      ```
* `delete/petshop/<id>` - Deleta petshop por id (DELETE)

## Pet
* `get/all/pet/` - Retorna todos os pets (GET)
* `get/pet/<id>/` - Busca de pet por id (GET)
* `create/pet/` - Criação de pet (POST)
    * Exemplo de corpo da requisição para criação:
      
      ```
      {
            "nome_pet": "Bolinha",
            "especie": "Hamster"
      }
      ```
* `update/pet/<id>/` - Atualização de todo o objeto pet (PUT)
    * Exemplo de corpo da requisição para atualização completa:
      
      ```
      {
            "nome_pet": "Safira",
            "especie": "Cachorro"
      }
      ```
* `update/pet/<id>/` - Atualização parcial (PATCH)
    * Exemplo de corpo da requisição para atualização completa:
      
      ```
      {
            "especie": "Gato"
      }
      ```
* `delete/pet/<id>` - Deleta pet por id (DELETE)

