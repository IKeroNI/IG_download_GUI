from re import T
import instaloader
import time ,os
import numpy as np
from random import randint, choice, randrange
from datetime import datetime
import logging
from math import ceil
from pathlib import Path
import functools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from itertools import islice, dropwhile, takewhile

def CheckIT():
    pass
    if not os.path.exists(plik+"\\info"):
        os.makedirs(plik+"\\info")
    if not os.path.exists(plik+"\\settings\\settings.txt"):
        if not os.path.exists(plik+"\\settings"):
            os.makedirs(plik+"\\settings")
        f=open(plik+"\\settings\\settings.txt","x")
        f.close()

        default_path_for_info_files = plik + "\\info"
        default_path_for_photos = plik
        default_path_for_settings = plik + "\\settings"
        default_path_for_session_files = plik + "\\instaloader_accounts"
        dict_for_settings = {
            "settings": default_path_for_settings,
            "session_files": default_path_for_session_files,
            "default_path": default_path_for_photos,
            "information_about_download": default_path_for_info_files,
        }
        with open(default_path_for_settings + "\\settings.txt", "a") as f: 
             for key, value in dict_for_settings.items(): 
                f.write('%s: %s\n' % (key, value))
             f.close()
        


class Ui_MainWindow(QtWidgets.QMainWindow):

    has_been_called = False

    def checkbox_method(self):
        pass

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
#        loadUi(default_path_for_settings + "\\test3.ui",self)



    def start_click(self):
        self.checkBox.stateChanged.connect(self.checkbox_method)
        WantDates = self.checkBox.isChecked()
        WantFirstDownload = self.checkBox_czypierwszyraz.isChecked()
        WantLongDownload = self.checkBox_long_download.isChecked()
        QtCore.QCoreApplication.quit
        from PyQt5.QtCore import pyqtRemoveInputHook
        pyqtRemoveInputHook()


        if self.browsefiles.has_been_called:
            default_path_for_session_files_posrednik = Path(fname)
            default_path_for_session_files = str(default_path_for_session_files_posrednik)
            session_file_path = "session_files"
            # opening a text file
            file1 = open(default_path_for_settings+"\\settings.txt", "r")
            
            # setting flag and index to 0
            index_default_path = 0
            
            # Loop through the file line by line
            for line in file1:  
                index_default_path += 1 
                
                # checking string is present in line or not
                if session_file_path in line:
                    break 

            file1.close()
            file1 = open(default_path_for_settings+"\\settings.txt", "r")
            list_of_lines = file1.readlines()
            list_of_lines[index_default_path-1] = "session_files: "+ default_path_for_session_files + "\n"

            file1.close() 

            file1 = open(default_path_for_settings+"\\settings.txt", "w")
            file1.writelines(list_of_lines)
            file1.close()

        if self.browsefiles2.has_been_called:
            default_path_for_photos_posrednik = Path(fname2)
            default_path_for_photos = str(default_path_for_photos_posrednik)

            string_def_path = 'default_path'

            file1 = open(default_path_for_settings+"\\settings.txt", "r")
            
            # setting flag and index to 0
            index_default_path = 0
            
            # Loop through the file line by line
            for line in file1:  
                index_default_path += 1 
                
                # checking string is present in line or not
                if string_def_path in line:
                    break 

            file1.close()
            file1 = open(default_path_for_settings+"\\settings.txt", "r")
            list_of_lines = file1.readlines()
            list_of_lines[index_default_path-1] = "default_path: "+ default_path_for_photos + "\n"

            file1.close() 

            file1 = open(default_path_for_settings+"\\settings.txt", "w")
            file1.writelines(list_of_lines)
            file1.close()

        plik = os.path.dirname(__file__)

        with open(plik+"\\settings\\settings.txt") as f:
            d = {str(k): v for line in f for (k, v) in [line.strip().split(":", 1)]}

        for key in list(d.keys()):
            if key == 'session_files':
                default_path_for_session_files = d[key].strip()
            if key == 'information_about_download':
                default_path_for_info_files = d[key].strip()
            if key == 'default_path':
                default_path_for_photos =d[key].strip()






        app = QtCore.QCoreApplication(sys.argv)
        #CzasStart = time.localtime()
        CzasStart = datetime.now()
        print("Download begins at: ", CzasStart.strftime( "%d/%m/%Y %H:%M:%S "))


        def swapPositions(list, pos1, pos2):
            
            # Oba elementy do zamiany, usun z pierwotnych miejsc i wloz do zmiennej
            first_ele = list.pop(pos1)  
            second_ele = list.pop(pos2-1)
            
            # Wloz w konkretne miejsca
            list.insert(pos1, second_ele) 
            list.insert(pos2, first_ele) 
            
            return list


        #Main

        try:

            # utworz plik
            date = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
            nazwa_pliku = f"filename_{date}"
            print(nazwa_pliku)
            save_path = default_path_for_info_files        


            file_name = nazwa_pliku + ".txt"
            completeName = os.path.join(save_path, file_name)
            print(completeName)

            with open(default_path_for_settings + '\\lista_user_prywatni.txt', 'r') as plik_do_with:
                lista_user_prywatni = [line.strip() for line in islice(plik_do_with,3,None)]
            with open(default_path_for_settings + '\\lista_user_ogolni.txt', 'r') as plik_do_with:
                lista_user_ogolni = [line.strip() for line in islice(plik_do_with,3,None)]




            session_file_names = ""
            L = instaloader.Instaloader()

            
            #L.load_session_from_file(USER,path_session_files)
            #if wybor in {"tak","t"}:
            if WantFirstDownload:
                for n in lista_user_ogolni:

                    L.interactive_login(n)
                    print("Password passed for: ",n)
                    merge = "".join([default_path_for_session_files,'\\','session-',n])
                    L.save_session_to_file(merge)
                    
                for n in lista_user_prywatni:

                    L.interactive_login(n)
                    print("Password passed for: ",n)
                    merge = "".join([default_path_for_session_files,'\\','session-',n])
                    L.save_session_to_file(merge)
            
            # listy osoby, do pobrania - fullCombo pobiera wszystko, priorytetowa - zdjecia, druga - zdjecia ogolnodostepne
            with open(default_path_for_settings + '\\lista1.txt', 'r') as load_file:
                #next(f) # omin pierwsza linijke
                lista_fullCombo = [line.strip() for line in islice(load_file,3,None)] #pierwsze 3 linijki pomija przy wczytywaniu | na tutorial
            
            with open(default_path_for_settings+'\\lista2.txt', 'r') as load_file:
                lista_priorytetowa = [line.strip() for line in islice(load_file,3,None)]
            with open(default_path_for_settings+'\\lista3.txt', 'r') as load_file:
                lista_druga = [line.strip() for line in islice(load_file,3,None)]

            nr1 = len(lista_fullCombo)
            nr2 = len(lista_priorytetowa)
            nr3 = len(lista_druga)

            print("nr1 nr2 nr3: ",nr1,nr2,nr3)

            x = len(lista_fullCombo)
            y = len(lista_priorytetowa)
            z = len(lista_druga)

            if WantDates:
                temp_since = self.dateEdit_MAX.dateTime()
                temp_until = self.dateEdit_MIN.dateTime()
                SINCE = temp_since.toPyDateTime()
                UNTIL = temp_until.toPyDateTime()

            lista_iteracji = ["x","y","z"]
            while x > 0 or y > 0 or z > 0:

                print("Starting while loop: ")

                if x == 0:   #w tych if-ach chcę wykluczyć te listy, które już nie mają zmiennych do pobrania, czyli kiedy lista jest pusta
                    lista_iteracji.remove("x")
                    x = -1
                    print("Usunalem X")
                if y == 0:
                    lista_iteracji.remove("y")
                    y = -1
                    print("Usunalem Y")
                if z == 0:
                    lista_iteracji.remove("z")
                    z = -1
                    print("Usunalem Z")

                if not lista_iteracji:
                    continue
                wybor = choice(lista_iteracji)


                if wybor == "x": #and x != nr1:

                        print("entering loop X (List1)")
                        losowanko = np.random.choice(lista_user_prywatni,replace=True)
                        file_nameY ="session-" + losowanko
                        konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                        L.load_session_from_file(losowanko,konkretny_path_session_file) # tutaj do wywalenia w razie W ___________________________________________
                        CheckLength=len(lista_fullCombo)
                        k=randint(0,x-1)
                        print("Downloading: " + lista_fullCombo[k])
                        file1 = open(completeName, "a")
                        file1.write('Lista fullCombo,' + lista_fullCombo[k])
                        file1.write("\n")
                        file1.close()
                        L.dirname_pattern=default_path_for_photos+"\\"+lista_fullCombo[k]

                        if WantDates:
                            profile = instaloader.Profile.from_username(L.context, lista_fullCombo[k]).get_posts()
                        
                            for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, profile)):
                                L.download_post(post, lista_fullCombo[k])
                        


                        elif WantLongDownload:
                            profile = instaloader.Profile.from_username(L.context, lista_fullCombo[k])
                            posts_sorted_by_likes = sorted(profile.get_posts(),
                                        key=lambda p: p.likes + p.comments,
                                        reverse=True)
                            X_percentage = int(self.lineEdit.text())
                            licznik = 1
                            licznik_zmiany_konta = 0
                            for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
                                if licznik % 14 == 0:
                                    losowanko = np.random.choice(lista_user_prywatni,replace=True)
                                    file_nameY ="session-" + losowanko
                                    konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                                    L.load_session_from_file(losowanko,konkretny_path_session_file)
                                    licznik_zmiany_konta=licznik_zmiany_konta+1
                                L.download_post(post, lista_fullCombo[k])
                                licznik +=1

                        else:
                            L.download_profile(lista_fullCombo[k],download_stories=True)

                        if CheckLength > 1:
                            swapPositions(lista_fullCombo,k,CheckLength-1)
                        lista_fullCombo.pop()  
                        x -= 1
                        print("x(lista_priorytetowa) contains " + str(x) + " elements")

                elif wybor == "y":
                        print("Entering List2")
                        losowanko = np.random.choice(lista_user_prywatni,replace=True)
                        file_nameY ="session-" + losowanko
                        konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                        L.load_session_from_file(losowanko,konkretny_path_session_file) # tutaj do wywalenia w razie W ___________________________________________
                        CheckLength=len(lista_priorytetowa)
                        k=randint(0,y-1)
                        print("Downloading: " + lista_priorytetowa[k])
                        file1 = open(completeName, "a")
                        file1.write('Lista priorytetowa,' + lista_priorytetowa[k])
                        file1.write("\n")
                        file1.close()

                        L.dirname_pattern=default_path_for_photos+"\\"+lista_priorytetowa[k]

                        if WantDates:
                                profile = instaloader.Profile.from_username(L.context, lista_priorytetowa[k]).get_posts()
                                for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, profile)):
                                    L.download_post(post, lista_priorytetowa[k])
                        elif WantLongDownload:
                            profile = instaloader.Profile.from_username(L.context, lista_priorytetowa[k])
                            posts_sorted_by_likes = sorted(profile.get_posts(),
                                        key=lambda p: p.likes + p.comments,
                                        reverse=True)
                            X_percentage = int(self.lineEdit.text())
                            licznik = 1
                            licznik_zmiany_konta = 0
                            for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
                                if licznik % 14 == 0:
                                    losowanko = np.random.choice(lista_user_prywatni,replace=True)
                                    file_nameY ="session-" + losowanko
                                    konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                                    L.load_session_from_file(losowanko,konkretny_path_session_file)
                                    licznik_zmiany_konta=licznik_zmiany_konta+1
                                L.download_post(post, lista_priorytetowa[k])
                                licznik +=1
                            


                        else:
                            L.download_profile(lista_priorytetowa[k],download_stories=True,fast_update=True,)

                        if CheckLength > 1:
                            swapPositions(lista_priorytetowa,k,CheckLength-1)
                        
                        usuwanie = lista_priorytetowa.pop()  
                        y -= 1

                        print("y contains: " + str(y))


                elif wybor == "z": 

                        print("Entering list3 (open profiles)")
                        losowanko = np.random.choice(lista_user_ogolni,replace=True)
                        file_nameY ="session-" + losowanko
                        konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                        L.load_session_from_file(losowanko,konkretny_path_session_file)
                        if z <= nr3-6:  # po ilu pobraniach chcemy wprowadzic czekanie, jak jest wiecej kont dostepnych, to mozna odjąć większą liczbę.
                            print("Czekam")
                            time.sleep(randint(10,100))
                        CheckLength=len(lista_druga)
                        k=randint(0,z-1)
                        L.download_videos = False
                        print("Downloading: " + lista_druga[k])
                        file1 = open(completeName, "a")
                        file1.write('Lista druga,' + lista_druga[k])
                        file1.write("\n")
                        file1.close()

                        L.dirname_pattern=default_path_for_photos+"\\"+lista_druga[k]

                        if WantDates:
                            profile = instaloader.Profile.from_username(L.context, lista_druga[k]).get_posts()
                            
                        
                            for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, profile)):
                                L.download_post(post, lista_druga[k])

                        elif WantLongDownload:
                            profile = instaloader.Profile.from_username(L.context, lista_druga[k])
                            posts_sorted_by_likes = sorted(profile.get_posts(),
                                        key=lambda p: p.likes + p.comments,
                                        reverse=True)
                            X_percentage = int(self.lineEdit.text())
                            licznik_zmiany_konta = 0
                            licznik = 1
                            for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
                                if licznik % 14 == 0:
                                    losowanko = np.random.choice(lista_user_ogolni,replace=True)
                                    file_nameY ="session-" + losowanko
                                    konkretny_path_session_file = os.path.join(default_path_for_session_files, file_nameY)
                                    L.load_session_from_file(losowanko,konkretny_path_session_file)
                                    licznik_zmiany_konta=licznik_zmiany_konta+1
                                L.download_post(post, lista_druga[k])
                                licznik +=1
                            
                            file1 = open(completeName, "a")
                            file1.write('Account change: ' + str(licznik_zmiany_konta))
                            file1.write("\n")
                            file1.close()
                        else:

                            L.download_profile(lista_druga[k],download_stories=True,fast_update=True)

                        if CheckLength > 1:
                            swapPositions(lista_druga,k,CheckLength-1)
                                            
                        lista_druga.pop()  
                        z -= 1
                        print("z(lista_priorytetowa) contains " + str(z) + " elements")  

            else:
                print("End of loop")

            CzasKoniec = datetime.now()
            print("End of download: ", CzasKoniec.strftime( "%d/%m/%Y %H:%M:%S "))

            #Rożnica w czasach
            diff = CzasKoniec - CzasStart
            # Zamien różnice na sekundy, i zamien na minuty
            diff_in_minutes = diff.total_seconds() / 60
            print('Download took: ' + str(diff_in_minutes))   

            #zapis do pliku wartosci w minutach calego procesu

            file1 = open(completeName, "a")
            file1.write('Whole process took: ' + str(diff_in_minutes) + " minutes")
            file1.close()
            time.sleep(5)
            quit()

        except Exception as Argument:
        
            file_name2 = nazwa_pliku + "_error.txt"

            completeName2 = os.path.join(save_path, file_name2)
            file2 = open(completeName2, "a")
        

            file2.write(str(Argument))
            file2.close()

    
    def zakoncz_clicked(self):
        print("Wylaczam") # we will just print clicked when the button is pressed
        time.sleep(5)
        quit()

    def browsefiles(self):
        Ui_MainWindow.browsefiles.has_been_called = True
        global browsefiles1Check
        browsefiles1Check = True
        path_session_files_main = plik
        global fname
        fname = QtWidgets.QFileDialog.getExistingDirectory(self,'Open file',path_session_files_main)
        self.lineEdit_sessionfile.setText(fname)
    
    def browsefiles2(self):
        Ui_MainWindow.browsefiles2.has_been_called = True
        global browsefiles2Check
        browsefiles2Check = True
        path_session_files_main = plik
        global fname2
        fname2 = QtWidgets.QFileDialog.getExistingDirectory(self,'Open file',path_session_files_main)
        self.lineEdit_folder_ze_zdjeciami.setText(fname2)

    def lista1_click(self):
        save_path1 = default_path_for_settings
        nazwa_pliku = "lista1.txt"
        completeName1 = os.path.join(save_path1, nazwa_pliku)
        #completeName1 = save_path1 + "lista1.txt"
        lista1_txt = open(completeName1, "a")
        lista1_txt.close()
        os.startfile(completeName1)
        


    def lista2_click(self):
        save_path2 = default_path_for_settings
        nazwa_pliku = "lista2.txt"
        completeName2 = os.path.join(save_path2, nazwa_pliku)
        #completeName1 = save_path1 + "lista1.txt"
        lista1_txt = open(completeName2, "a")
        lista1_txt.close()
        os.startfile(completeName2)
    def lista3_click(self):
        save_path3 = default_path_for_settings
        nazwa_pliku = "lista3.txt"
        completeName3 = os.path.join(save_path3, nazwa_pliku)
        #completeName1 = save_path1 + "lista1.txt"
        lista1_txt = open(completeName3, "a")
        lista1_txt.close()
        os.startfile(completeName3)

    def lista_user_prywatni_click(self):
        save_path3 = default_path_for_settings
        nazwa_pliku = "lista_user_prywatni.txt"
        completeName3 = os.path.join(save_path3, nazwa_pliku)
        #completeName1 = save_path1 + "lista1.txt"
        lista1_txt = open(completeName3, "a")
        lista1_txt.close()
        os.startfile(completeName3)

    def lista_user_ogolni_click(self):
        save_path3 =  default_path_for_settings # r'C:\Users\User\Desktop\instaloader'
        nazwa_pliku = "lista_user_ogolni.txt"
        completeName3 = os.path.join(save_path3, nazwa_pliku)
        #completeName1 = save_path1 + "lista1.txt"
        lista1_txt = open(completeName3, "a")
        lista1_txt.close()
        os.startfile(completeName3)


    def onStateChange(self, state):
        if state == QtCore.Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox_long_download.setChecked(False)
            elif self.sender() == self.checkBox_long_download:
                self.checkBox.setChecked(False)      

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(370, 320, 241, 101))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start_click)


        self.checkBox_czypierwszyraz = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_czypierwszyraz.setGeometry(QtCore.QRect(410, 210, 161, 61))
        self.checkBox_czypierwszyraz.setObjectName("checkBox_czypierwszyraz")
        

        self.lista3 = QtWidgets.QPushButton(self.centralwidget)
        self.lista3.setGeometry(QtCore.QRect(50, 80, 191, 61))
        self.lista3.setObjectName("lista3")
        self.lista3.clicked.connect(self.lista3_click)

        self.lista2 = QtWidgets.QPushButton(self.centralwidget)
        self.lista2.setGeometry(QtCore.QRect(50, 160, 191, 61))
        self.lista2.setObjectName("lista2")
        self.lista2.clicked.connect(self.lista2_click)
        
        self.lista1 = QtWidgets.QPushButton(self.centralwidget)
        self.lista1.setGeometry(QtCore.QRect(50, 240, 191, 61))
        self.lista1.setObjectName("lista1")
        self.lista1.clicked.connect(self.lista1_click)


        self.zakoncz = QtWidgets.QPushButton(self.centralwidget)
        self.zakoncz.setGeometry(QtCore.QRect(50, 320, 191, 101))
        self.zakoncz.setObjectName("zakoncz")
        self.zakoncz.clicked.connect(self.zakoncz_clicked)


        self.lineEdit_sessionfile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sessionfile.setGeometry(QtCore.QRect(450, 120, 113, 20))
        self.lineEdit_sessionfile.setObjectName("lineEdit_sessionfile")
        self.lineEdit_folder_ze_zdjeciami = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_folder_ze_zdjeciami.setGeometry(QtCore.QRect(450, 150, 113, 20))
        self.lineEdit_folder_ze_zdjeciami.setObjectName("lineEdit_folder_ze_zdjeciami")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 270, 81, 20))
        self.lineEdit.setObjectName("lineEdit_percentage")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_2.setGeometry(QtCore.QRect(304, 120, 141, 23)) #browsfiles do session files
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.browsefiles)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget) #folder ze zdjeciami
        self.pushButton_3.setGeometry(QtCore.QRect(304, 150, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.browsefiles2)


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)#button_user_prywatny
        self.pushButton_5.setGeometry(QtCore.QRect(200, 505, 121, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.lista_user_prywatni_click)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget) #button_user_ogolny
        self.pushButton_6.setGeometry(QtCore.QRect(50, 505, 121, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.lista_user_ogolni_click)


        date = QtWidgets.QDateEdit(self)
        date.setGeometry(100, 100, 150, 40)
        d = QtCore.QDate(2020, 6, 10)
        date.setDate(d)

        self.dateEdit_MIN = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_MIN.setGeometry(QtCore.QRect(370, 520, 110, 22))
        self.dateEdit_MIN.setObjectName("dateEdit_MIN")
        self.dateEdit_MIN.setDate(QtCore.QDate.currentDate())



        self.dateEdit_MAX = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_MAX.setGeometry(QtCore.QRect(510, 520, 110, 22))
        self.dateEdit_MAX.setObjectName("dateEdit_MAX")
        self.dateEdit_MAX.setDate(QtCore.QDate.currentDate())
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(380, 500, 141, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_long_download = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_long_download.setGeometry(QtCore.QRect(410, 210, 141, 17))
        self.checkBox_long_download.setObjectName("checkBox_long_download")


        self.lineEdit.setReadOnly(self.checkBox_long_download.checkState()!=QtCore.Qt.Unchecked)
        self.checkBox_long_download.stateChanged.connect(lambda state: self.lineEdit.setReadOnly(state!=QtCore.Qt.Checked))
        self.checkBox_long_download.stateChanged.connect(self.lineEdit.clear)


        self.checkBox.stateChanged.connect(self.onStateChange)
        self.checkBox_long_download.stateChanged.connect(self.onStateChange)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 520, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 520, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 260, 141, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")

        self.label_tytul = QtWidgets.QLabel(self.centralwidget)
        self.label_tytul.setGeometry(QtCore.QRect(70, 10, 521, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_tytul.setFont(font)
        self.label_tytul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tytul.setObjectName("label_tytul")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpcje = QtWidgets.QMenu(self.menubar)
        self.menuOpcje.setObjectName("menuOpcje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpcje.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.checkBox_czypierwszyraz.setText(_translate("MainWindow", "First time use"))
        self.lista3.setText(_translate("MainWindow", "List 3"))
        self.lista2.setText(_translate("MainWindow", "List 2"))
        self.lista1.setText(_translate("MainWindow", "List 1"))
        self.zakoncz.setText(_translate("MainWindow", "Close"))
        self.pushButton_2.setText(_translate("MainWindow", "Select path for session files"))
        self.pushButton_3.setText(_translate("MainWindow", "Folder for photos"))
        self.pushButton_5.setText(_translate("MainWindow", "Private Accounts"))
        self.pushButton_6.setText(_translate("MainWindow", "Open Accouts"))
        self.checkBox.setText(_translate("MainWindow", "Download from interval: "))
        self.checkBox_long_download.setText(_translate("MainWindow", "Turn on long download"))
        self.menuOpcje.setTitle(_translate("MainWindow", "Options"))
        self.label.setText(_translate("MainWindow", "to"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_tytul.setText(_translate("MainWindow", "Instagram Downloader v0.1 2022"))
        self.label_3.setText(_translate("MainWindow", "What percentage of photos\n"
"do you want to download?"))
    











if __name__ == "__main__":
    import sys
    global plik
    plik = os.path.dirname(__file__)
    os.chdir(plik)

    CheckIT()
    Ui_MainWindow.browsefiles2.has_been_called = False
    Ui_MainWindow.browsefiles.has_been_called = False

    
    default_path_for_settings = plik + "\\settings"
    default_path_for_session_files = plik + "\\instaloader_accounts"
    default_path_for_info_files = plik + "\\info"

    #wczytuje defaulty z pliku
    with open(plik+"\\settings\\settings.txt") as f:
        d = {str(k): v for line in f for (k, v) in [line.strip().split(":", 1)]}


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







