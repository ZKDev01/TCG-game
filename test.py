import random 

from src.game import Game
from src.combat import combat_between_cards 

from src.models.player import (
  Card,
  Player
)






def test() -> None:
  N = 40
  deck1 = [ Card(f"Deck.1-Card.{i}", random.randint(1,10), random.randint(1,10)) for i in range(N) ]
  deck2 = [ Card(f"Deck.2-Card.{i}", random.randint(1,10), random.randint(1,10)) for i in range(N) ]

  player1 = Player(deck1, 10)
  player2 = Player(deck2, 10)

  for card in player1.deck:
    print(card)

if __name__ == '__main__':
  test()
