from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition

class Screen1(MDScreen):

    def go_pie_chart(self):
        self.parent.parent.go_piechart()
        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'piechart'
        self.parent.transition = SlideTransition(direction='right')


    def go_addscreen(self):

        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'addscreen'
        self.parent.transition = SlideTransition(direction='right')
    def go_camera(self):

        self.parent.transition = SlideTransition(direction="left")

        self.parent.current ='camerascreen'
        self.parent.transition = SlideTransition(direction='right')
    def go_picture(self):

        self.parent.transition = SlideTransition(direction="left")

        self.parent.current = 'screen2'
        self.parent.transition = SlideTransition(direction='right')

