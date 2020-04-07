
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.app import App

class FL(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def player (self):
        sound = SoundLoader.load("sound.wav")
        if sound:
            sound.play()

class application(App):
    def build(self):
        self.icon = "logo.png"
        return FL()

if __name__ == "__main__":
    application().run()