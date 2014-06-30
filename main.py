from kivy.app import App
from kivy.core.audio import Sound,SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from pygame import mixer
from kivy.clock import Clock
import itertools

class AudioModule(Sound):
    def __init__(self):
        mixer.init()

    def load(self,audio):
        mixer.music.load(audio)

    def play(self):
        if self.get_pos() > 0:
            mixer.music.unpause()
        else:
            mixer.music.play()
        super(AudioModule,self).play()


    def pause(self):
        mixer.music.pause()


    def get_pos(self):
        return mixer.music.get_pos()
    

    def is_playing(self):
        if mixer.music.get_busy()  == True:
            return True
        else:
            return False

SoundLoader.register(AudioModule)

class Loader(Popup):
    load = ObjectProperty()

class Main(BoxLayout):
    song_title = ObjectProperty()
    play_button = ObjectProperty()
    def __init__(self):
        super(Main,self).__init__()
        self.sound = AudioModule()

    def show_popup(self):
        content = Loader(load=self.load_sound)
        self.p = Popup(title="Choose a File",content=content)
        self.p.open()

    def load_sound(self,audio):
        self.sound.load(audio[0])
        self.song_title.text = str(audio[0])
        self.p.dismiss()
        self._play()

    def _play(self):
        self.sound.play()

    def _pause(self):
        self.sound.pause()

class AudioPlayer(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    AudioPlayer().run()
