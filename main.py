
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6 import QtSql
import time
from frm_root import Ui_root
from newpwd_1 import Ui_Form as Ui_Form_2
from pwewdgt2 import Ui_pweingabe_wdgt_2
from genpwd_1 import Ui_Form as Ui_Form_3
from chkpwd_1 import Ui_Form as Ui_Form_4
from chpw import Ui_Form as Ui_Form_5
from pw_incorrect import Ui_Warnung
from show_pw_frm import Ui_Form as Ui_Form_1_2
import subprocess
import hashlib
import secrets
import string
import os
from entpwd1 import Ui_Form as Ui_Form
from editpwfrm import Ui_Form as Ui_Form_6
from editpwfrm_2 import Ui_Form as Ui_Form_7
from tresorpassworteingabe import Ui_Form as Ui_Form_8


class frm_entpwd(QMainWindow, Ui_Form):
    global datei
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bst.clicked.connect(self.clckd)
    def clckd(self):
        entrytext=self.lineEdit.text()
        hex_hash=hashlib.sha256(entrytext.encode())
        hash=hex_hash.hexdigest()
        hex_hash=hashlib.sha256(hash.encode())
        hash=hex_hash.hexdigest()
        file=open("GKEY.txt", "r")
        content=file.read()
        if (hash==content):
            self.close()
            file="aescrypt.exe -d -p "+ entrytext + " Passwords.txt.aes"
            subprocess.getoutput(file)
            time.sleep(2)
            global datei
            os.popen("anz.py")
            time.sleep(2)
            os.remove("Passwords.txt")
        else:
            wrng.show()
        self.lineEdit.clear()           
class frm_warning(QMainWindow, Ui_Warnung):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.buttonBox.clicked.connect(self.close) 
lg=""
pw=""
us=""
class frm_addpwd(QMainWindow, Ui_Form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_abort.clicked.connect(self.close)
        self.bt_ok.clicked.connect(self.key_entering)
    def key_entering(self):
        entry_login_text=self.entry_login.text()
        entry_pw_text=self.entry_pw.text()
        entry_using_text=self.entry_using.text()
        global lg 
        global pw
        global us
        lg='Benutzername: ' + entry_login_text
        pw='Passwort: ' + entry_pw_text
        us='Verwendung: ' + entry_using_text
        self.entry_login.clear()
        self.entry_pw.clear()
        self.entry_using.clear()       
        eingabefeld.show()
class frm_addpwd2(QMainWindow, Ui_pweingabe_wdgt_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_ok_2.clicked.connect(self.add)
    def add(self):
        plntext=self.entry_pw_2.text()
        hshtxt=hashlib.sha256(plntext.encode())
        hshtxt=hshtxt.hexdigest()
        hshtxt=hashlib.sha256(hshtxt.encode())
        hshtxt=hshtxt.hexdigest()
        file=open("GKEY.txt", "r")
        content=file.read()
        if (hshtxt==content):
            self.close()
            file="aescrypt.exe -d -p "+ plntext + " Passwords.txt.aes"
            subprocess.getoutput(file)
            time.sleep(2)
            fl=open("Passwords.txt", "a")                      
            fl.write(lg)
            fl.write("\n")
            fl.write(pw)
            fl.write("\n")
            fl.write(us)
            fl.write("\n\n")
            fl.close()
            open("Zwischendatei.txt", "w").write("") 
            file2 = "aescrypt.exe -e -p " + plntext + " Passwords.txt"           
            subprocess.getoutput(file2)
            time.sleep(2)
            os.remove("Passwords.txt")
            open("Zwischendatei.txt", "w").write("")
        else:
            wrng.show()
        self.entry_pw_2.clear()
class frm_genpwd(QMainWindow, Ui_Form_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generate.clicked.connect(self.gnr)
    def gnr(self):
        self.pw_generated.clear()
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        pwd_length = 12
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        while True:
            pwd = ''
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))
            if (any(char in special_chars for char in pwd) and 
                sum(char in digits for char in pwd)>=2):
                    break
            self.pw_generated.setText(pwd)
class frm_chkpwd(QMainWindow, Ui_Form_4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check.clicked.connect(self.cnedt_chk)
    def cnedt_chk(self):
        self.sec_step.setText("")
        cnter1=0
        inh=self.entpw.text()
        strg = inh 
        print(list(strg))
        if (any(c in string.ascii_lowercase for c in inh)==True):
            cnter1=cnter1+1
        if (any(c in string.ascii_uppercase for c in inh)):
            cnter1=cnter1+1
        if (any(c in string.digits for c in inh)):
            cnter1=cnter1+1
        if (any(c in string.punctuation for c in inh)):
            cnter1=cnter1+1
        if (len(inh)>5):
            cnter1=cnter1+2
        if (len(inh)>=8):
            cnter1=cnter1+4
        lbt=str(cnter1)
        self.sec_step.setText(lbt + "/10")
        self.entpw.clear()
class frm_chgkey(QMainWindow, Ui_Form_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.ch)
    def ch(self):
        global oldpw
        global newpw
        oldpw=self.lineEdit.text()
        newpw=self.lineEdit_2.text()
        hshtxt=hashlib.sha256(oldpw.encode())
        hshtxt=hshtxt.hexdigest()
        hshtxt=hashlib.sha256(hshtxt.encode())
        hshtxt=hshtxt.hexdigest()
        file=open("GKEY.txt", "r")
        content=file.read()
        if (hshtxt==content):
            self.close()
            file="aescrypt.exe -d -p "+ oldpw + " Passwords.txt.aes"
            subprocess.getoutput(file)
            time.sleep(2)
            gk=open("GKEY.txt", "w")
            hshtxt=hashlib.sha256(newpw.encode())
            hshtxt=hshtxt.hexdigest()
            hshtxt=hashlib.sha256(hshtxt.encode())
            hshtxt=hshtxt.hexdigest()
            gk.write(hshtxt)                                               
            file2 = "aescrypt.exe -e -p " + newpw + " Passwords.txt"           
            subprocess.getoutput(file2)
            time.sleep(2)
            os.remove("Passwords.txt")
            open("Zwischendatei.txt", "w").write("")
        else:
            wrng.show()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
class frm_entpwd_2(QMainWindow, Ui_Form_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#------------------------------------------------------------------------------------------------
class frm_edit(QMainWindow, Ui_Form_6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bst.clicked.connect(self.editpw)
    def editpw(self):
        entrytext=self.lineEdit.text()
        hex_hash=hashlib.sha256(entrytext.encode())
        hash=hex_hash.hexdigest()
        hex_hash=hashlib.sha256(hash.encode())
        hash=hex_hash.hexdigest()
        file=open("GKEY.txt", "r")
        content=file.read()
        if (hash==content):
            
            self.close()
            
            file="aescrypt.exe -d -p "+ entrytext + " Passwords.txt.aes"
            subprocess.getoutput(file)
            time.sleep(2)
            os.popen("Passwords.txt")
            var=subprocess.getoutput("tasklist.exe")
            
            while ("notepad" in var):
                var=subprocess.getoutput("tasklist.exe")
                time.sleep(2)
            print("Fertihg")
            file="aescrypt.exe -e -p "+ entrytext + " Passwords.txt"
            subprocess.getoutput(file)
            os.remove("Passwords.txt")
            
        else:
            wrng.show()
        self.lineEdit.clear()      

class frm_edit2(QMainWindow, Ui_Form_7):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

#------------------------------------------------------------------------------------------------

class frm_trs(QMainWindow, Ui_Form_8):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bst.clicked.connect(self.checkpw)
    def checkpw(self):
        entrytext=self.lineEdit.text()
        hex_hash=hashlib.sha256(entrytext.encode())
        hash=hex_hash.hexdigest()
        hex_hash=hashlib.sha256(hash.encode())
        hash=hex_hash.hexdigest()
        print(os.getcwd())
        file=open("GKEY.txt", "r")
        content=file.read()
        if (hash==content):
            self.close()
            filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            ".\\Tresor\\"
            
            )
            
            for file in (os.listdir(".\\Tresor\\")):
                try:
                    os.chdir(".\\Tresor\\")
                except:
                    break
                if not (".aes" in file):
                    file2="aescrypt.exe -e -p "+ entrytext + f" '{file}'"
                    print(file2)
                    subprocess.getoutput(file2)
                    time.sleep(1)
                    print(os.getcwd())
                    os.remove(file)

            os.popen(filename)

        else:
            wrng.show()
        self.lineEdit.clear()           



class Root(QMainWindow, Ui_root, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ntp)
        self.pushButton_2.clicked.connect(self.adp)
        self.pushButton_3.clicked.connect(self.gnp)
        self.pushButton_4.clicked.connect(self.ckp)
        self.pushButton_5.clicked.connect(self.chp)
        self.pushButton_6.clicked.connect(self.edp)
        self.pushButton_7.clicked.connect(self.tre)
        self.actionBeenden.triggered.connect(self.close)
        self.actionDokumentation.triggered.connect(self.doku)
    def doku(self):
        pass
        
    def ntp(self):
        frm_ntpw.show()

    def adp(self):
        frm_adpw.show()
    def gnp(self):
        frm_gnp.show()
    def ckp(self):
        frm_ckp.show()
    def chp(self):
        frm_chpw.show()
    def edp(self):
        frm_edtpw.show()
    def tre(self):
        frm_tres.show()

    
    
        

        

app=QApplication()
root=Root()
root.show()
#----------------Frames für direkte Unterwigets der QMainWindow-Klasse------------------
frm_ntpw=frm_entpwd()
frm_adpw=frm_addpwd()
frm_gnp=frm_genpwd()
frm_ckp=frm_chkpwd()
frm_chpw=frm_chgkey()
frm_edtpw=frm_edit()
frm_tres=frm_trs()
frm_edtpw_2=frm_edit2()
#----------------Ende Frames------------------------------------------------------------
wrng=frm_warning() 

#-----------------Klasse entpwd--------------------------------------
eingabefeld=frm_addpwd2()
app.exec()
    
        

