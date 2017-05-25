from kivy.app import App
from kivy.uix.widget import Widget

class MemeScreen(Widget):
    pass

class heeliesApp(App):
    def build(self):
        return MemeScreen()

if __name__ == '__main__':
    heeliesApp().run()
