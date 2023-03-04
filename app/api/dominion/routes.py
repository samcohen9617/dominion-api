"""Dominion routes"""
import json
from .blueprint import BP
from .controllers import get_cards_controller, scrape_cards_controller


@BP.route('/cards', methods=['GET'])
def get_cards():
    """Get cards route"""
    return json.loads(get_cards_controller())

@BP.route('/scrape', methods=['GET'])
def get_cards():
    """Get cards route"""
    return json.loads(scrape_cards_controller())