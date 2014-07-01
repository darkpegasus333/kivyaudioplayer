from kivy.app import App
from kivy.core.audio import Sound,SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy import platform
import os

if platform == "android":
    import android.mixer as mixer
else:
    from pygame import mixer

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


class Loader(BoxLayout):
        load = ObjectProperty(None)
        cancel = ObjectProperty(None)


class Main(BoxLayout):
    song_title = ObjectProperty()
    play_button = ObjectProperty()
    def __init__(self):
        super(Main,self).__init__()
        self.sound = AudioModule()

    def show_popup(self):
        content = Loader(load=self.load_sound, cancel=self.dismiss_popup)
        self.p = Popup(title="Choose a File",content=content)
        self.p.open()

    def dismiss_popup(self):
        self.p.dismiss()

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
        SoundLoader.register(AudioModule)
        return Main()

if __name__ == '__main__':
    AudioPlayer().run()
