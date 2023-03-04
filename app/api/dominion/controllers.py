from app import db
from bson.json_util import dumps
import requests
from bs4 import BeautifulSoup


def get_cards_controller():
    """Get cards controller"""
    cards = db.get_collection("cards")
    return dumps(cards.find({}))


def format_text(cell):
    for img in cell.findAll('img'):
        img.replace_with(img['alt'])
    return cell.text

def get_cards_from_table(soup):
    table = soup.find('table', {'class': 'wikitable sortable'})
    table_headers = [cell.text.lower().strip() for cell in table('th')]
    table_data = [[cell for cell in row("td")] for row in table("tr")]
    table_data.pop(0)

    cards_arr = []
    for row in table_data:
        row_dict = {}
        for i in range(len(row)):
            # name cell
            if i == 0:
                print(row[i].text)
                cell = row[i].text
            else:
                cell = format_text(row[i])
            row_dict[table_headers[i]] = cell.strip()
        cards_arr.append(row_dict)
    return cards_arr


def scrape_cards_controller():
    url = 'http://wiki.dominionstrategy.com/index.php/List_of_cards'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    cards = db.get_collection("cards")
    cards.delete_many({})
    cards.insert_many(get_cards_from_table(soup))