# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(905, 824)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 902, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(20, -1, 20, -1)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.passowrd = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.passowrd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passowrd.setObjectName("passowrd")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passowrd)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.progressBar = QtWidgets.QProgressBar(parent=self.gridLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.progressBar)
        self.gridLayout.addLayout(self.formLayout_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(450, 80))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, -1, 20, -1)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.passowrdType = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.passowrdType.setObjectName("passowrdType")
        self.passowrdType.addItem("")
        self.passowrdType.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passowrdType)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.passowrdLenght = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.passowrdLenght.setObjectName("passowrdLenght")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passowrdLenght)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.specialChar = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.specialChar.setObjectName("specialChar")
        self.verticalLayout.addWidget(self.specialChar)
        self.number = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.number.setObjectName("number")
        self.verticalLayout.addWidget(self.number)
        self.capitalChards = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.capitalChards.setObjectName("capitalChards")
        self.verticalLayout.addWidget(self.capitalChards)
        self.easter = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.easter.setObjectName("easter")
        self.verticalLayout.addWidget(self.easter)
        self.word = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.word.setObjectName("word")
        self.verticalLayout.addWidget(self.word)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verticalLayout)
        self.generate = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.generate.setObjectName("generate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.generate)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.Image = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.gridLayout.addWidget(self.Image, 3, 2, 1, 1)
        self.generatedpassword = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.generatedpassword.setText("")
        self.generatedpassword.setScaledContents(False)
        self.generatedpassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.generatedpassword.setObjectName("generatedpassword")
        self.gridLayout.addWidget(self.generatedpassword, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Hasło"))
        self.label_7.setText(_translate("Dialog", "Moc hasła"))
        self.label.setText(_translate("Dialog", "Generowanie hasła"))
        self.label_2.setText(_translate("Dialog", "Sprawdzanie hasła"))
        self.label_4.setText(_translate("Dialog", "Typ hasła"))
        self.passowrdType.setItemText(0, _translate("Dialog", "Hasło"))
        self.passowrdType.setItemText(1, _translate("Dialog", "Pin"))
        self.label_5.setText(_translate("Dialog", "Długość"))
        self.label_6.setText(_translate("Dialog", "Wymagania"))
        self.specialChar.setText(_translate("Dialog", "Znaki specjalne"))
        self.number.setText(_translate("Dialog", "Cyfry"))
        self.capitalChards.setText(_translate("Dialog", "Duże litery"))
        self.easter.setText(_translate("Dialog", "Zając wielkanocny"))
        self.word.setText(_translate("Dialog", "Słowo"))
        self.generate.setText(_translate("Dialog", "Generuj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
