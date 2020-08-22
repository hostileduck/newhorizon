# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 521)
        MainWindow.setStyleSheet("QLabel{\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"    background-position: center;  \n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: whitesmoke;\n"
"    background-position: center;\n"
"    \n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: #DC143C;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 70, 301, 311))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: white;\n"
"    background-position: center;\n"
"    \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 30, 81, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"    background-position: center;  \n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 250, 91, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: #DC143C;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 100, 161, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: #DC143C;\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 170, 161, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: #DC143C;\n"
"}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Horizon System"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit.setText(_translate("MainWindow", "ID"))
        self.lineEdit_2.setText(_translate("MainWindow", "PASS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
