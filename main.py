#Source Root of A root
from kivymd.app import MDApp
#Initialize Ads for Android
from kivmob import KivMob
from kivymd.theming import ThemeManager
#Kivy import

from kivy.clock import mainthread
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import certifi
# Hiding Debugs
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.animation import Animation
if platform == 'macosx':

    Window.size = (450, 750)
    #if you use macosx you will be resized like this
else:
    pass
class OneApp(MDApp):
    try:
        ads = KivMob('ca-app-pub-1818238534900904~2025018602')

        def __init__(self):
            try:
                super().__init__()
                #Declaring MDApp object
                self.theme_cls  = ThemeManager()
                self.theme_cls.primary_palette =  'Orange'

                self.theme_cls.primary_style = 'Light'
                self.title = 'Type To Write'
                self.screen = Builder.load_file('main.kv')



                self.setup()

                # Put Banner Ads
            except:
                pass



        def animate_card(self,widget,text_field,spinn):
            anim = Animation(pos_hint={'center_y':0.53})

            anim.start(widget)
            anim1 = Animation(pos_hint={'center_y':0.75})
            anim1.start(text_field)
            anim2 = Animation(pos_hint={'center_y':0.65})
            anim2.start(spinn)


        def picture_taken(self, obj, filename):

            try:
                self.picture = filename
                from google.cloud import storage

                """Uploads a file to the bucket."""
                bucket_name = 'online-server-test'
                destination_blob_name = "test-storage-blob.png"
                debug = True
                if not debug:
                    storage_client = storage.Client()
                else:
                    cred_file = 'key.json'
                    storage_client = storage.Client.from_service_account_json(cred_file)

                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob(destination_blob_name)

                blob.upload_from_filename(self.picture)
                print(
                    "File {} uploaded to {}.".format(
                        self.picture, destination_blob_name
                    )
                )

                self.hit_cloud_function(destination_blob_name)
                self.screen.ids.firebaseloginscreen.display_loading_screen()


            except:
                pass

        @mainthread
        def hit_cloud_function(self, blob_name):

            try:
                from urllib.parse import urlencode
                msg_data = urlencode({'message': blob_name})
                headers = {'Content-type': 'application/x-www-form-urlencoded',
                           'Accept': 'text/plain'}

                print("Sending trigger request")
                trigger_url = "https://us-central1-endless-theorem-297112.cloudfunctions.net/detect_handwriting"
                UrlRequest(trigger_url, req_body=msg_data, req_headers=headers, ca_file=certifi.where(),
                           on_failure=self.error, on_error=self.error, on_success=self.success)
            except:
                pass

        def error(self, *args):
            try:
                print("Error", args)
            except:
                pass

        def success(self, request, response):

            print("Success!")
            try:
                self.screen.ids.typetowritescreen.change_values(response)
                self.hide_screen()
                self.screen.ids.typetowritescreen.change_screen('screen1')
            except:
                pass

        def setup(self):
            try:

                self.screen.ids.firebaseloginscreen.web_api_key = "AIzaSyBmrGpiwimYZ-HT_BSesv4gMjuPJcG3omM"
                self.screen.ids.firebaseloginscreen.debug = False
                self.screen.ids.firebaseloginscreen.remember_user = True
                self.screen.ids.firebaseloginscreen.require_email_verification = True
            except:
                pass
        def call(self,button):
            if button.icon == 'typewriter':

                try:
                    self.screen.ids.typetowritescreen.check_data_login()
                except:
                    pass


            if button.icon == 'notebook':
                try:
                    self.screen.ids.typetowritescreen.grammar_check()
                except:
                    pass
            if button.icon == 'google-photos':
                try:
                    self.screen.ids.typetowritescreen.see_recent_images()
                except:
                    pass



            if button.icon == 'camera':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_camera()
                except:
                    pass

            if button.icon == 'ship-wheel':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_addscreen()
                except:
                    pass

            if button.icon == 'content-save':
                try:
                    self.screen.ids.typetowritescreen.make_json()
                except:
                    pass

            if button.icon == 'view-list':
                try:
                    self.screen.ids.typetowritescreen.visualize_json()


                    self.screen.ids.typetowritescreen.ids.addscreen.go_friend()
                except:
                    pass

            if button.icon == 'exit-to-app':
                try:
                    self.screen.ids.typetowritescreen.ids.addscreen.go_back()
                except:
                    pass

            if button.icon == 'delete':
                try:
                    self.screen.ids.typetowritescreen.delete()
                except:
                    pass
            if button.icon == 'email-alert':
                try:
                    self.screen.ids.typetowritescreen.change_email()
                except:
                    pass
            if button.icon == 'chart-bar':
                try:
                    self.screen.ids.typetowritescreen.ids.screen1.go_pie_chart()
                except:
                    pass
            if button.icon == 'truck-delivery':
                try:
                    self.screen.ids.typetowritescreen.change_screen('ongkirscreen')
                except:
                    pass







        def show_dialog(self):
            try:
                #Make A PopUp Dialog to warn user
                self.dialog = MDDialog(title='LOGOUT', text='Are you sure to log out',
                                       size_hint=(0.5, 1),
                                       buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)
                                           , MDRaisedButton(text='Sign Out', on_release=self.sign_out)])
                #Show It On The Screen
                self.dialog.open()
            except:
                pass

        def making_banner(self):
            try:
                self.ads.new_banner('ca-app-pub-1818238534900904/4048546717', top_pos=False)
                # Requesting New Ads

                self.ads.request_banner()
                from plyer import uniqueid
                self.ads.add_test_device(uniqueid.id.decode('utf-8'))
                self.ads.show_banner()
            except:
                pass
        def close_dialog(self,*args):
            #Closing Dialog
            try:
                self.dialog.dismiss()
            except:
                pass

        def sign_out(self, obj):
            #Make Firebase To Be Logged Out
            try:

                self.screen.ids.firebaseloginscreen.log_out()
                self.screen.current = "firebaseloginscreen"
                self.dialog.dismiss()
            except:
                pass
        def loading_screen(self,*args):
            #Show The Loading Screen
            try:
                self.screen.ids.firebaseloginscreen.display_loading_screen()
            except:
                pass

        def hide_screen(self,*args):
            #Hide The Loading Screen
            try:
                self.screen.ids.firebaseloginscreen.hide_loading_screen()
            except:
                pass

        def on_resume(self):
            self.ads.request_banner()






        def build(self):
            try:
                self.making_banner()
                self.screen.ids.typetowritescreen.setup()

                self.screen.ids.typetowritescreen.ids.ongkirscreen.ids.search_provinsi.setup()
                self.screen.ids.typetowritescreen.store_data_online()
            except:
                pass










            return self.screen
            # Showing Ads To The Screen


    except:
        pass




if __name__ == '__main__':
    OneApp().run()

