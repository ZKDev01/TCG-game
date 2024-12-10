import kivy
kivy.require ("1.9.2")

from kivy.app import App
from kivy.uix.widget import Widget


class GameWidget (Widget):
  None


class DeployApp (App):
  title= "TCG Prototype"

  def build(self):
    return GameWidget()



if __name__ == '__main__':
  app = DeployApp()
  app.run()
