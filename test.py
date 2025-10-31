import requests
import json

character = "galbrena"

base_url= "https://www.prydwen.gg/page-data/wuthering-waves/characters/{character}/page-data.json"

def fetch_character_data(name):
    url = f"{base_url}".format(character=name)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Character not found"}
    
def endgameStats(data):
    stats = data['result']['data']['currentUnit']['nodes'][0]['endgameStats']['raw']
    parsed = json.loads(stats)
    formatted_stats = {}
    for stat in parsed['content'][0]['content']:
        stat_name = stat['content'][0]['content'][0]['value'].strip(': ')
        stat_value = stat['content'][0]['content'][1]['value']
        formatted_stats[stat_name] = stat_value
    
    return formatted_stats

if __name__ == "__main__":
    data = fetch_character_data(character)
    print(endgameStats(data))