from typing import List
from random import shuffle

from src.models.card import Card



class Player:
  def __init__(self, deck:List[Card], life:int):
    self.deck = deck
    self.life = life
    shuffle(self.deck)
    self.hand = deck[:5]
  


