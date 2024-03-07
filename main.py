from typing import List, Dict
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()
teams = {}
registered_pokemons = {}
keys = ["id","weight","height"]


class Pokemon:
    def __init__(self, name: str, pokemon_data: Dict):
        self.id = pokemon_data["id"]
        self.name = name
        self.weight = pokemon_data["weight"]
        self.height = pokemon_data["height"]


class Team:
    def __init__(self, owner: str, pokemons: List[Pokemon]):
        self.owner = owner
        self.pokemons = pokemons


def get_pokemon(pokemon_name: str) -> Dict:
    if pokemon_name in registered_pokemons:
            pokemon = registered_pokemons[pokemon_name]
    else:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if response.status_code != 200:
            return None
        pokemon_data = response.json()
        if pokemon_data is None:
            raise HTTPException(status_code=400, detail=f"Pokemon '{pokemon_name}' não encontrado")
        pokemon_data = {key: pokemon_data[key] for key in keys}
        pokemon = Pokemon(pokemon_name, pokemon_data)
        registered_pokemons[pokemon_name] = pokemon

    return pokemon


@app.post("/api/teams")
async def create_team(team_data: Dict):
    owner = team_data.get("user")
    team_list = team_data.get("team")
    if not owner or not team_list:
        raise HTTPException(status_code=400, detail="O usuário e o seu time devem ser informados")
    
    if len(team_list) > 6:
        raise HTTPException(status_code=400, detail="Um time não pode possuir mais de 6 Pokemons")

    pokemon_instances = []
    for pokemon_name in team_list:
        pokemon_name = pokemon_name.lower()
        pokemon = get_pokemon(pokemon_name)
        pokemon_instances.append(pokemon)
    
    team_id = len(teams) + 1
    teams[team_id] = Team(owner, pokemon_instances)
    return {"message": "Time criado com sucesso", "team_id": team_id}


@app.get("/api/teams")
async def get_all_teams():
    return teams


@app.get("/api/teams/{team_id}")
async def get_team_by_id(team_id: int):
    if team_id not in teams:
        raise HTTPException(status_code=404, detail=f"Time de id {team_id} não foi encontrado")
    return teams[team_id]