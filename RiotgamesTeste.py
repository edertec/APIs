import requests

def get_summoner_rank(summoner_name):
    api_key = 'C0D3F4398699BD76BC085E41E04B77D6'  # Substitua pela sua chave da API
    region = 'br1'
    
    summoner_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
    
    response = requests.get(summoner_url)
    if response.status_code == 200:
        summoner_data = response.json()
        summoner_id = summoner_data['id']

        ranked_url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}"
        
        ranked_response = requests.get(ranked_url)
        if ranked_response.status_code == 200:
            ranked_data = ranked_response.json()
            for obj in ranked_data:
                if obj['queueType'] == 'RANKED_SOLO_5x5':
                    return obj
    return None

summoner_rank = get_summoner_rank('Ashe')
print(summoner_rank)