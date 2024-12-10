from src.models.card import Card


def combat_between_cards (card1:Card, card2:Card) -> None:
  card1.defense = min( 0, card1.defense - card2.attack )
  card2.defense = min( 0, card2.defense - card1.attack )

