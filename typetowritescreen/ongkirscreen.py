from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition

from kivy.properties import NumericProperty,BooleanProperty
from kivy.uix.textinput import TextInput
class MyTextInput(TextInput):
    size_hint = (None, None)
    height = NumericProperty(50)
    readonly = BooleanProperty(False)
    multiline = BooleanProperty(False)

    with open('data/easyversion.json', 'r') as f:
        import json
        word_list = json.load(f)
        word_list = list(word_list.keys())

    def setup(self):
        self.bind(text=self.on_text)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """ Add support for tab as an 'autocomplete' using the suggestion text.
        """

        if self.suggestion_text and keycode[1] == 'enter' :

            self.insert_text(self.suggestion_text + ' ')
            return True

        return super(MyTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)

    def on_text(self, instance, value):
        """ Include all current text from textinput into the word list to
        emulate the same kind of behavior as sublime text has.
        """

        self.suggestion_text = ''
        word_list = list(set(
            self.word_list + value[:value.rfind(' ')].split(' ')))
        val = value[value.rfind(' ') + 1:]
        if not val:
            return
        try:
            # grossly inefficient just for demo purposes
            word = [word for word in word_list
                    if word.startswith(val)][0][len(val):]

            if not word:
        
                return

            self.suggestion_text = word


        except IndexError:
            print('Index Error.')




    

class OngkirScreen(MDScreen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.parent.change_screen('screen1')
        self.ids.image.source = ''
        self.ids.label.text = ''
        self.ids.weight.text = ''
        self.ids.province.text = 'Provinsi Asal'
        self.ids.kota.text ='Kota Asal'
        self.ids.province_tujuan.text = 'Provinsi Tujuan'
        self.ids.kota_tujuan.text = 'Kota Tujuan'
        self.ids.kurir.text = "Kurir"
        self.parent.transition = SlideTransition(direction='left')



