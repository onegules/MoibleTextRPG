from kivy.app import App
from kivy.uix.widget import Widget

class MobileGame(Widget):
    pass

class MobileApp(App):
    def build(self):
        return MobileGame()

if __name__=='__main__':
    MobileApp().run()
