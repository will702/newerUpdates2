#Kivy Import
from kivy.uix.screenmanager import Screen
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import  ListProperty
#Nulis Import
from . import nulis
# KivyMD imports
import requests

from kivymd.uix.list import ImageLeftWidget,ThreeLineListItem
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import  MDRaisedButton,MDFlatButton
# Python imports
import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
import os.path
from calendar import monthrange
import datetime
import json
from datetime import date
#Initialize Screen Design
folder = os.path.dirname(os.path.realpath(__file__))#Get Absolute Path
Builder.load_file(folder + "/screen1.kv")
Builder.load_file(folder + "/screen2.kv")
Builder.load_file(folder+  "/camerascreen.kv")
Builder.load_file(folder+"/addscreen.kv")
Builder.load_file(folder+'/friendscreen.kv')
Builder.load_file(folder+'/piechart.kv')
Builder.load_file(folder+'/editscreen.kv')
Builder.load_file(folder+'/ongkirscreen.kv')

Builder.load_file(folder + "/typetowritescreen.kv")
#Import Screen

import screen_import

#Import Python Module

import firebase_admin
class TypeToWriteScreen(Screen):

    try:
        #Data Integration


        selection = ListProperty([])
        images = ListProperty(['img/jne.jpg','img/tiki.jpg','img/pos.jpg'])
        kurirs = ListProperty(['img/jne.jpg','img/tiki.jpg','img/pos.jpg','img/anteraja.png','img/sicepat.jpg','img/wahana.jpg','img/lion.jpg','img/ninja.png','img/jnt.jpg'])
        with open('data/date.json', 'r') as f:

            attempts = json.load(f)
        with open('data/easyversion.json','r') as f:

            data_tables = json.load(f)

        with open('data/data.json', 'r')as fp:
            data = json.load(fp)

       #Add Item To The List
        def change_image_resi(self,args):
            if args.lower() == 'jne':

                self.ids.addscreen.ids.image.ii = self.kurirs[0]

            if args.lower() == 'tiki':
                self.ids.addscreen.ids.image.ii = self.kurirs[1]
            if args.lower() == 'pos':
                self.ids.addscreen.ids.image.ii = self.kurirs[2]
            if args.lower() == 'jnt':
                self.ids.addscreen.ids.image.ii = self.kurirs[8]
            if args.lower() == 'ninja':
                self.ids.addscreen.ids.image.ii = self.kurirs[7]
            if args.lower() == 'lion':
                self.ids.addscreen.ids.image.ii =self.kurirs[6]
            if args.lower() == 'anteraja':
                self.ids.addscreen.ids.image.ii = self.kurirs[3]
            if args.lower() == 'wahana':
                self.ids.addscreen.ids.image.ii = self.kurirs[5]
            if args.lower() == 'sicepat':
                self.ids.addscreen.ids.image.ii = self.kurirs[4]

        def visualize_json(self):



            self.ids.friendscreen.ids.container.clear_widgets()

            for i in self.data.keys():

                if self.data[i]['kurir'] == 'jne':

                    image = ImageLeftWidget(source=self.kurirs[0])

                if self.data[i]['kurir'] == 'tiki':
                    image = ImageLeftWidget(source=self.kurirs[1])
                if self.data[i]['kurir'] == 'pos':
                    image = ImageLeftWidget(source=self.kurirs[2])
                if self.data[i]['kurir'] == 'jnt':
                    image = ImageLeftWidget(source=self.kurirs[8])
                if self.data[i]['kurir'] == 'ninja':
                    image = ImageLeftWidget(source=self.kurirs[7])
                if self.data[i]['kurir'] == 'lion':
                    image = ImageLeftWidget(source=self.kurirs[6])
                if self.data[i]['kurir'] == 'anteraja':
                    image = ImageLeftWidget(source=self.kurirs[3])
                if self.data[i]['kurir'] == 'wahana':
                    image = ImageLeftWidget(source=self.kurirs[5])
                if self.data[i]['kurir'] == 'sicepat':
                    image = ImageLeftWidget(source=self.kurirs[4])



                isi = TwoLineAvatarListItem(text=self.data[i]['kurir'].upper(), on_press=lambda x, item=i: self.show_dialog5(text=item),secondary_text=i)
                isi.add_widget(image)

                self.ids.friendscreen.ids.container.add_widget(isi)








        def setup(self):




            self.ids.ongkirscreen.ids.province_tujuan.values = list(self.data_tables.keys())

            self.ids.ongkirscreen.ids.province.values = list(self.data_tables.keys())




        def show_kota(self,text):
            try:


                self.ids.ongkirscreen.ids.kota_tujuan.text = 'Kota Tujuan'


                self.ids.ongkirscreen.ids.kota_tujuan.values =  list(self.data_tables[text].keys())
            except:
                pass
        def show_kota1(self,text):
            try:

                self.ids.ongkirscreen.ids.kota.text = 'Kota'


                self.ids.ongkirscreen.ids.kota.values = list(self.data_tables[text].keys())
            except:
                pass












        def hitung(self):

            toast("Counting..........")
            try:
                from rajaOngkirApi import rajaongkirApi
                api =  rajaongkirApi(key='23930140f7b47aaebf5318262ee5d0f1',accountType='starter')



                self.id_origin = self.data_tables[self.ids.ongkirscreen.ids.province.text][self.ids.ongkirscreen.ids.kota.text]


                self.id_destinasi = self.data_tables[self.ids.ongkirscreen.ids.province_tujuan.text][self.ids.ongkirscreen.ids.kota_tujuan.text]
                print(self.id_origin, self.id_destinasi)
                if bool(self.ids.ongkirscreen.ids.weight.text) == False:
                    from kivymd.uix.snackbar import Snackbar
                    snackbar = Snackbar(text="Harap Isi Semuanya", duration=0.5)
                    snackbar.show()
                else:
                    harga = api.requestApi(origin=self.id_origin, destination=self.id_destinasi, weight=str(self.ids.ongkirscreen.ids.weight.text), courier=self.ids.ongkirscreen.ids.kurir.text.lower())
                    harga = harga.decode('utf-8')


                    harga = json.loads(harga)
                    deskripsi = ''
                    for i in ((harga['rajaongkir']['results'][0]['costs'])):
                        if 'HARI' in i["cost"][0]["etd"]:


                            deskripsi+=f' {i["service"]} : Rp {i["cost"][0]["value"]} \n Perkiraan {i["cost"][0]["etd"]}\n'


                        else:
                            print(f'{i["cost"][0]["etd"]}')
                            deskripsi += f' {i["service"]} : Rp {i["cost"][0]["value"]} \n Perkiraan {i["cost"][0]["etd"]} hari\n'

                    if self.ids.ongkirscreen.ids.kurir.text.lower() == 'jne':

                        self.ids.ongkirscreen.ids.image.ii = self.images[0]

                    if self.ids.ongkirscreen.ids.kurir.text.lower() == 'tiki':

                        self.ids.ongkirscreen.ids.image.ii = self.images[1]
                    if self.ids.ongkirscreen.ids.kurir.text.lower() == 'pos':

                        self.ids.ongkirscreen.ids.image.ii = self.images[2]
                    if deskripsi == '':
                        self.ids.ongkirscreen.ids.label.text = 'tidak ada kurir yang tersedia'
                    if deskripsi != '':
                        self.ids.ongkirscreen.ids.label.text = deskripsi
            except:
                from kivymd.uix.snackbar import Snackbar
                snackbar = Snackbar(text="Harap Isi Semuanya", duration=0.5)
                snackbar.show()








        def update_dict(self):
            currentMonth = datetime.datetime.now().month
            currentYear = datetime.datetime.now().year
            new = self.get_datetime_range(currentYear,currentMonth)
            new = [str(i)for i in new]

            with open ('data/date.json','r')as fppp:

                self.attempts = json.load(fppp)
            try:
                for i in self.attempts.copy().keys():

                    if  i not in new:
                        del self.attempts[i]
            except:
                pass


            with open ('data/date.json','w') as fppppp:
                json.dump(self.attempts,fppppp)





        def get_datetime_range(self,year, month):
            nb_days = monthrange(year, month)[1]

            return [datetime.date(year, month, day) for day in range(1, nb_days + 1)]

        def copy_details(self,details):
            Clipboard.copy(details)

        def set_label(self):
            mydate = datetime.datetime.now()

            self.ids.piechart.label.text = f'Total Usages In {(mydate.strftime("%B"))}'

        def change_screen(self, screen, *args):

            self.ids.screen_manager.current = screen



        def make_json(self):
            from tes import check_resi
            try:
                if self.ids.addscreen.ids.no_resi.text in self.data:
                    from kivymd.uix.snackbar import Snackbar
                    self.snackbar = Snackbar(text="Sudah Ad Resi Yg Sama", duration=0.5)
                    self.snackbar.show()
                else:
                    if check_resi(self.ids.addscreen.ids.kurir.text.lower(),self.ids.addscreen.ids.no_resi.text)['error'] == True:
                        from kivymd.uix.snackbar import Snackbar
                        self.snackbar = Snackbar(text="Salah Resi Atau Salah Kurir", duration=0.5)
                        self.snackbar.show()
            except KeyError:
                if self.ids.addscreen.ids.no_resi.text in self.data:
                    from kivymd.uix.snackbar import Snackbar
                    self.snackbar = Snackbar(text="Sudah Ad Resi Yg Sama", duration=0.5)
                    self.snackbar.show()
                else:
                    with open('data/data.json','w') as f:

                        from kivymd.uix.snackbar import Snackbar
                        self.snackbar = Snackbar(text="Details Saved", duration=1.0)
                        self.snackbar.show()
                        self.data[self.ids.addscreen.ids.no_resi.text] = {}
                        self.data[self.ids.addscreen.ids.no_resi.text]['kurir'] = self.ids.addscreen.ids.kurir.text.lower()

                        print(self.data)
                        json.dump(self.data,f)
                        self.visualize_json()
                        self.ids.addscreen.go_friend()



        def show_dialog5(self,*args,text):


            from tes import check_resi
            deskripsi = check_resi(self.data[text]['kurir'],text)
            self.deskripsi = deskripsi["data"]["detail"]
            self.dialog = MDDialog(title='DETAILS', text=f'PENERIMA: {self.deskripsi["receiver"]}\n'
                                                         f'STATUS: {self.deskripsi["status"]}\n'
                                                         f'DIKIRIM: {self.deskripsi["date_shipment"]}\n'
                                                         f'DITERIMA: {self.deskripsi["date_received"]}\n'



                                   ,

                                   size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),MDFlatButton(text='Delete',on_release=lambda x ,item=text:self.delete(item))
                                       ,MDRaisedButton(text='See Details',on_release=lambda x ,item=text:self.change_name(text=item))])

            self.dialog.open()






        def delete(self,*name):
            try:
                name = name[0]
                toast('Delete Success')
                del self.data[name]
                with open('data/data.json','w') as f:

                    json.dump(self.data,f)
                self.visualize_json()
                self.close_dialog()
            except:
                pass



        def change_name(self,*args,text):
            print(text)
            self.change_screen('editscreen')
            self.dialog.dismiss()
            self.deskripsi['history'].reverse()
            self.ids.editscreen.ids.container.clear_widgets()
            for i in self.deskripsi['history']:


                isi = ThreeLineListItem(text=i["position"],secondary_text=i["time"],tertiary_text=i["desc"],on_press=lambda  x, item=i:self.copy_details(
                    f'{i["position"]}\n'
                    f'{i["time"]}\n'
                    f'{i["desc"]}'
                ))

                self.ids.editscreen.ids.container.add_widget(isi)



        def default(self,*args):

            self.ids.screen1.spinn.text = '1' #Make Value To Default

            self.ids.screen1.spinn1.text = '1'#Make Value To Default

            self.dialog2.dismiss()#Close The Dialog

        def grammar_check(self):
            import os,certifi
            os.environ['SSL_CERT_FILE'] = certifi.where()
            try:


                toast('Wait Indexing Grammar....')

                from .grammar_check import grammar



                self.ids.screen1.isi.text = grammar(self.ids.screen1.isi.text)

            except:
                pass



        def change_spinn(self):
            try:
                if self.ids.ongkirscreen.ids.search_provinsi.text in list(self.data_tables.keys()):

                    self.ids.ongkirscreen.ids.province.text = self.ids.ongkirscreen.ids.search_provinsi.text
                    from kivymd.uix.snackbar import Snackbar
                    snackbar = Snackbar(text="Provinsi Ditemukan", duration=1)
                    snackbar.show()
                if self.ids.ongkirscreen.ids.search_provinsi.text not in list(self.data_tables.keys()):
                    from kivymd.uix.snackbar import Snackbar
                    snackbar = Snackbar(text="Provinsi Tidak Ditemukan", duration=1)
                    snackbar.show()
            except:
                pass


        def change_spinn1(self):

            try:
                if self.ids.ongkirscreen.ids.search_provinsi_tujuan.text in list(self.data_tables.keys()):



                    self.ids.ongkirscreen.ids.province_tujuan.text = self.ids.ongkirscreen.ids.search_provinsi_tujuan.text
                    from kivymd.uix.snackbar import Snackbar
                    snackbar = Snackbar(text="Provinsi Ditemukan", duration=1)
                    snackbar.show()
                if self.ids.ongkirscreen.ids.search_provinsi_tujuan.text not in list(self.data_tables.keys()):
                    from kivymd.uix.snackbar import Snackbar
                    snackbar = Snackbar(text="Provinsi Tidak Terjangkau", duration=1)
                    snackbar.show()
            except:
                pass




        def change_values(self,output):
            self.ids.screen1.isi.text = output


        def check_data_login(self):


            self.get_permission()





            toast('Load Module....')




            try:
                nama = self.ids.screen1.username.text
                self.ids.screen1.username.text = ''
                kelas = self.ids.screen1.kelas.text
                self.ids.screen1.kelas.text = ''
                font = self.ids.screen1.spinn.text
                self.ids.screen1.spinn.text = 'Font'
                kertas = self.ids.screen1.spinn1.text
                self.ids.screen1.spinn1.text = 'Paper'

                isi = self.ids.screen1.isi.text
                self.ids.screen1.isi.text = ''
                with open('data/date.json', 'r') as f:

                    self.attempts = json.load(f)



                    try:
                        pass



                    except KeyError:
                        with open('data/date.json', 'w') as fpp:
                            self.attempts[str(date.today())] = 0

                            json.dump(self.attempts, fpp)

                with open ('data/date.json','w') as f:


                    try:
                        self.attempts[str(date.today())]+=1

                        json.dump(self.attempts,f)
                    except KeyError:
                        with open('data/date.json', 'w') as fpp:
                            self.attempts[str(date.today())] = 0

                            json.dump(self.attempts, fpp)

                            self.attempts[str(date.today())]+= 1

                            json.dump(self.attempts, f)



                prs = nulis.Fung(isi, kertas, font, nama, kelas)

                prs.textNulis()

                self.ids.screen2.image1.source = prs.return_location()
                self.change_screen('screen2')
                print(self.ids.screen_manager.current)
            except:
                self.dialog2 = MDDialog(title='No Input ', text='Fill Out The Font and Paper Section',
                                        size_hint=(0.5, 1),
                                        buttons=[MDFlatButton(text='Close', on_release=self.close_dialog2)
                                            , MDRaisedButton(text='Default', on_release=self.default)])

                self.dialog2.open()

        def go_piechart(self):
            #Making and Updating Chart
            self.update_dict()
            self.set_label()



            self.ids.piechart.make_piechart()
            self.ids.piechart.update_chart()












        def translation(self):

            try:
                self.get_permission()
                try:
                    from .translation_google import translating
                    toast("Translating...")


                    self.ids.screen1.isi.text = translating(self.ids.screen1.isi.text)
                except:
                    pass
            except:
                pass


        def see_recent_images(self):
            try:
                from kivymd.toast import toast
                toast("Load Image........")
                self.get_permission()
                from .check_recent import  check_recent
                self.ids.screen2.image1.source = check_recent()
                self.ids.screen1.go_picture()
            except:
                pass






        def close_dialog2(self,*obj):
            try:
                self.dialog2.dismiss()
            except:
                pass

        def get_permission(self):
            from .permission  import check_permission
            check_permission()



        def close_dialog(self, *obj):
            try:
                self.dialog.dismiss()
            except:
                pass

    except:
        pass