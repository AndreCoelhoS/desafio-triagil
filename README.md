# Desafio Triágil - API de Times de Pokémon

Este projeto implementa uma API usando FastAPI e Python 3.10.12 para gerenciar times de Pokémon. Ele permite que os usuários criem times, pesquisem times pela ID e obtenham uma lista de todos os times registrados.

## Rotas

- `GET /api/teams`: Retorna todos os times registrados.
- `GET /api/teams/{team_id}`: Retorna o time de id `team_id`.
- `POST /api/teams`: Cria um novo time com base nos dados fornecidos no corpo da solicitação.

## Requisitos

### Classes

- `Pokemon`: Representa um Pokémon com suas informações básicas.
- `Team`: Representa um time de Pokémon, contendo um proprietário e uma lista de Pokémon.

### Funcionalidades

- Os Pokémon são buscados na pokeAPI (pokeapi.co) para obter seus dados.
- Os dados dos Pokémon (ID, peso e altura) são armazenados junto com o time.
- A API retorna uma mensagem de erro clara quando ocorre um problema.

## Executando o Projeto

1. Clone este repositório.
2. Certifique-se de ter o Docker instalado em sua máquina.
3. Navegue até o diretório do projeto.
4. Execute o seguinte comando para construir e iniciar o contêiner Docker:

```bash
docker-compose up --build
```

5. Acesse a API em `http://localhost:8000`.
6. É possível testar as rotas em `http://localhost:8000/docs`.

## Exemplo de Uso

### Criar um Time
```json
POST /api/teams
{
  "user": "andre",
  "team": [
    "articuno",
    "zapdos",
    "moltres",
    "mew",
    "mewtwo",
    "arceus"
  ]
}
```
```json
{
  "message": "Time criado com sucesso",
  "team_id": 1
}
```

### Obter Todos os Times Registrados
```json
GET /api/teams
```
```json
{
  "1": {
    "owner": "andre",
    "pokemons": [
      {
        "name": "articuno",
        "id": 144,
        "weight": 554,
        "height": 17
      },
      {
        "name": "zapdos",
        "id": 145,
        "weight": 526,
        "height": 16
      },
      {
        "name": "moltres",
        "id": 146,
        "weight": 600,
        "height": 20
      },
      {
        "name": "mew",
        "id": 151,
        "weight": 40,
        "height": 4
      },
      {
        "name": "mewtwo",
        "id": 150,
        "weight": 1220,
        "height": 20
      },
      {
        "name": "arceus",
        "id": 493,
        "weight": 3200,
        "height": 32
      }
    ]
  },
  "2": {
    "owner": "andre",
    "pokemons": [
      {
        "name": "mew",
        "id": 151,
        "weight": 40,
        "height": 4
      },
      {
        "name": "mewtwo",
        "id": 150,
        "weight": 1220,
        "height": 20
      }
    ]
  }
}
```

### Obter Time pela ID
```json
GET /api/teams/2
```
```json
{
  "owner": "andre",
  "pokemons": [
    {
      "name": "mew",
      "id": 151,
      "weight": 40,
      "height": 4
    },
    {
      "name": "mewtwo",
      "id": 150,
      "weight": 1220,
      "height": 20
    }
  ]
}
```
