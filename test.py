from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox
from time import *
def bt_click():
    ch=windows.le1.text()
    if (ch.isnumeric()==True):
        QMessageBox.critical(windows,"erreur","necessite alpha and numbers")
        windows.le1.clear()
    x=ch.find(":")
    while(x!=-1):
        ch = ch[:x]+ch[x+1:]
        x=ch.find(":")

    windows.res.setText(ch)
    
def bt_2_click():
    pass
app = QApplication([])
windows = loadUi ("C:/Users/Was Sim/Desktop/wifi/mac.ui")
windows.show()
windows.bt.clicked.connect ( bt_click )
windows.bt_2.clicked.connect ( bt_2_click )

app.exec_()