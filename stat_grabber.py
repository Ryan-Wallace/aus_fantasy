from bs4 import BeautifulSoup
import requests as requests
url = "https://aus.prestosports.com/sports/wbkb/2022-23/boxscores/20221103_g0yq.xml?view=boxscore"
def print_boxscore(url):
    my_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"}
    fetched_page = requests.get(url, headers = my_headers)

    soup = BeautifulSoup(fetched_page.text, "lxml")

    box_score = soup.find("section", "tab-panel active clearfix")

    for player in box_score.find_all("a", "player-name"):

        player_data = {}

        print(player.string)
        boxscore_stats = []
        for element in player.parent.parent.children:
            if element.string and len(element.string.strip()) != 0:
                boxscore_stats.append(element.string.strip())

        player_data.update({"player_name": player.string})
        player_data.update({"fgm": boxscore_stats[1].split("-")[0]})
        player_data.update({"fga": boxscore_stats[1].split("-")[1]})
        player_data.update({"3pm": boxscore_stats[2].split("-")[0]})
        player_data.update({"ftm": boxscore_stats[3].split("-")[0]})
        player_data.update({"fta": boxscore_stats[3].split("-")[1]})
        player_data.update({"reb": boxscore_stats[6]})
        player_data.update({"ast": boxscore_stats[7]})
        player_data.update({"stl": boxscore_stats[8]})
        player_data.update({"blk": boxscore_stats[9]})
        player_data.update({"to": boxscore_stats[10]})
        player_data.update({"pts": boxscore_stats[12]})

        print(player_data)

print_boxscore(url)