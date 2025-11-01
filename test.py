import requests

url = "https://guide-server.aki-game.net/introduction/info"
params = {
    "roleGbId": "1411",
    "id": "14007"
}

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://wuwaguide.kurogames.com",
    "priority": "u=1, i",
    "referer": "https://wuwaguide.kurogames.com/",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-language": "en",
    "x-token": "eyJjVWlkIjoiNTM1Nzc0NjQwIiwiY2hhbm5lbElkIjoxOCwiaW5uZXJUb2tlbiI6IjMwNTg5NjU3OWRlYjRmMDhiYTE0MjQxNWY4Njg3MWI3In0="
}

response = requests.get(url, headers=headers, params=params)

# print("Status:", response.status_code)
# print("JSON:", response.json())


list_url = "https://guide-server.aki-game.net/introduction/list"
list_res = requests.get(url, headers=headers, params=params)
print(list_res.json())
# write to file
with open("character_list.json", "w", encoding="utf-8") as f:
    f.write(list_res.text)
