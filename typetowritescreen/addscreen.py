from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
class AddScreen(MDScreen):
    def go_back(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = self.parent.current = "screen1"
        self.ids.no_resi.text = ""
        self.ids.kurir.text  = "KURIR"
        self.parent.transition = SlideTransition(direction="left")
    def go_friend(self):

        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'friendscreen'
        self.parent.transition = SlideTransition(direction='right')
