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
* GET - `/petshops/` - Retorna uma lista dos petshops
* GET - `/petshops/id:str` - Retorna um petshop
* POST - `/petshops/` - Criação de petshop
  * Exemplo de corpo da requisição para criação:
      
      ```
      {
            "nome_petshop": "Cantinho dos Bichinhos",
            "descricao": "O cantinho aconchegante onde os amigos peludos são tratados com carinho e atenção."
      }
      ```
* PUT - `/petshops/id:str` - Atualiza um petshop por id
    * Exemplo de corpo da requisição para atualização completa:
      
      ```
      {
            "nome_petshop": "AmigoFiel Pet Shop"",
            "descricao": "O paraíso dos animais de estimação, onde a felicidade deles é nossa prioridade."
      }
      ```
* PATCH - `/petshops/id:str` - Atualiza um petshop por id parcialmente
    * Exemplo de corpo da requisição para atualização parcial:
      
      ```
      {
             "nome_petshop": "Campina pet"
      }
      ```
* DELETE - `/petshops/id:str` - Deleta petshop por id

## Pet
* GET - `/pets/` - Retorna uma lista dos pets
* GET - `/pets/id:str` - Retorna um pet
* POST - `/pets/` - Criação de pet
  * Exemplo de corpo da requisição para criação:
      
      ```
      {
            "nome_pet": "Bolinha",
            "especie": "Hamster"
      }
      ```
* PUT - `/pets/id:str` - Atualiza um pet por id
    * Exemplo de corpo da requisição para atualização completa:
      
      ```
      {
            "nome_pet": "Safira",
            "especie": "Cachorro"
      }
      ```
* PATCH - `/pets/id:str` - Atualiza um pet por id parcialmente
    * Exemplo de corpo da requisição para atualização parcial:
      
      ```
      {
            "especie": "Gato"
      }
      ```
* DELETE - `/pets/id:str` - Deleta pet por id
