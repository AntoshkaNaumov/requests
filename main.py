import requests

class Heroes:

    def __init__(self, token):
        self.token = token

    def get(self, url_all):
        result = (requests.get(url) for url in url_all)
        return result

    def parser(self):
        spisok_man = []
        for item in self.get(urls):
            intelligence = item.json()
            for power_stats in intelligence['results']:
                spisok_man.append({
                    'name' : power_stats['name'],
                    'intelligence' : power_stats['powerstats']['intelligence'],
                    })

        intelligence_hero = 0 
        for hero in spisok_man:
            if intelligence_hero < int(hero['intelligence']):
                intelligence_hero = int(hero['intelligence'])
                name = hero['name']

        print(f'Самый умный герой {name}, интеллект: {intelligence_hero}')

if __name__ == '__main__':
    token = "2619421814940190"
    urls = [
    f'https://www.superheroapi.com/api.php/{token}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{token}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{token}/search/Captain%America',
    ]
    heroes = Heroes(token)
    heroes.get(urls)
    heroes.parser()