
class Card:
  
  def __init__(self, name:str, attack:int, defense:int):
    self.name = name
    self.attack = attack
    self.defense = defense

  def __repr__(self) -> str:
    return f"{self.name.capitalize()} [{self.attack}/{self.defense}]"