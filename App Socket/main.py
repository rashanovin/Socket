from websocket import create_connection
from PyQt5 import QtCore, QtGui, QtWidgets

import json


class Ui_Dialog(object):
    def __init__(self):
        self.x = 10
        self.y = 400

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 544)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setStyleSheet("QGroupBox{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px\n"
                                    "}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 400))
        self.scrollArea.setStyleSheet("background-color: rgb(217, 219, 236);\n"
                                      "border-radius:10px")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 371, 454))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
                                      "background-color: rgb(245, 247, 251);\n"
                                      "border-radius:20px\n"
                                      "}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setToolTip("")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(245, 247, 251);\n"
                                    "}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border-radius:5px;\n"
                                      "background-color:#004dfc;\n"
                                      "padding:7px;\n"
                                      "color:#ffffff\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "color:#004dfc;\n"
                                      "background-color:#bed9ec;\n"
                                      "\n"
                                      "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sources/right-arrow_active.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/sources/right-arrow.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.groupBox)

        self.pushButton.clicked.connect(self.sendKey)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def sendKey(self):
        question = self.lineEdit.text()
        q = question

        self.lineEdit.setText('')
        question = '<p style=\" color: #25255e; \">%s</p>' % question
        self.box = '<b style=\"  font:20px Calibri; padding:25px \">'f'{question}''</b>'
        self.textBrowser.append(self.box)

        global ws

        try:

            ws.send(q)
            answer = json.loads(ws.recv())['answer']
        except Exception as e:
            if str(e) in ["Connection to remote host was lost.", "cannot access local variable 'ws' where it is not "
                                                                 "associated with a value"]:

                ws = create_connection("ws://185.208.174.101:8000/admin/")
                try:

                    ws.send(q)
                    answer = json.loads(ws.recv())['answer']
                except Exception as e:

                    answer = 'جوابی برای کلمه ارسال شده وجود ندارد!'

            else:
                answer = 'جوابی برای کلمه ارسال شده وجود ندارد!'

        responce = '<span style=\" color: #bf0066;font:20px Calibri; padding:25px\">'f'{answer}''</span>'
        self.textBrowser.append(responce)

        liner = '<p style=\"  font:20px Calibri; padding:25px ' \
                '\">--------------------------------------------------------</p>'
        self.textBrowser.append(liner)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Socket"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", " Type a message"))
        self.pushButton.setText(_translate("Dialog", "  Send"))


if __name__ == "__main__":
    import sys

    try:

        ws = create_connection("ws://185.208.174.101:8000/admin/")
    except Exception as e:

        ws = None

    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget{
            background:#25255e;
        }
    """
    app.setStyleSheet(style)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
