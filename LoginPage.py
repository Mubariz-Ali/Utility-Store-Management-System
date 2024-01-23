import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QWidget
from All import *

import resources.Icons_rc

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="utility_management_system"
)


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Icons/logo1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setSpacing(152)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 40)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setMinimumSize(QtCore.QSize(0, 71))
        self.label1.setMaximumSize(QtCore.QSize(501, 16777215))
        self.label1.setSizeIncrement(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(0, 0, 255);r")
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setTextFormat(QtCore.Qt.RichText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1, 0, QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignVCenter)
        self.loginButton = QtWidgets.QPushButton(self.frame_2)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 0))
        self.loginButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
                                       "    background-color: rgb(0, 85, 255);\n"
                                       "    color: white;\n"
                                       "    border-width: 2px;\n"
                                       "    border-radius: 25px;\n"
                                       "    \n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    \n"
                                       "    background-color: rgb(148, 180, 255);\n"
                                       "    border-style: insert;\n"
                                       "}")
        self.loginButton.setIconSize(QtCore.QSize(16, 16))
        self.loginButton.setAutoRepeatInterval(100)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        self.verticalLayout_3.addWidget(self.loginButton, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        cursor = db.cursor()
        query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        results = cursor.fetchall()
        if results:
            for result in results:
                user_status = result[3]
                if user_status == 1:
                    QMessageBox.information(self, "Success", "Login Successful")
                    self.adminWindow()
                    return
                elif user_status == 0:
                    QMessageBox.information(self, "Success", "Login Successful")
                    self.staffWindow()
                    return
                else:
                    QMessageBox.warning(self, "Error", "Invalid Username or Password")
            else:
                QMessageBox.warning(self, "Error", "Invalid Username or Password")


    def adminWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.icons.hide()
        self.ui.menuButton.setChecked(True)

    def staffWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.icons.hide()
        self.ui.menuButton.setChecked(True)
        self.ui.adminButton_1.hide()
        self.ui.adminButton_2.hide()
        self.ui.userButton.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Utility-Store Management System"))
        self.label1.setText(_translate("MainWindow", "Utility Store Management System"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
