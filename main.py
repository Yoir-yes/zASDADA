import string
import sys
import random

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.generate.clicked.connect(self.generate)

		self.smallChar = [l for l in string.ascii_lowercase]
		self.capitalchar = [l for l in string.ascii_uppercase]
		self.numbers = [l for l in string.digits]
		self.specialChars = [l for l in string.punctuation]

	def generate(self):
		lenght = self.ui.passowrdLenght.text()
		type = self.ui.passowrdType.currentText()
		password = ''
		if type == "Pin":

			for i in range(int(lenght)):
				password += str(random.randint(0, 9))
		else:
			elements = [self.smallChar]
			if self.ui.specialChar.isChecked():
				elements.append(self.specialChars)
			if self.ui.number.isChecked():
				elements.append(self.numbers)
			if self.ui.capitalChards.isChecked():
				elements.append(self.capitalchar)
			for i in range(int(lenght)):
				type = random.randint(0,len(elements)-1)
				password += elements[type][random.randint(0, len(elements[type])-1)]

			if self.ui.easter.isChecked() and len(password) >= 5:
				max_index = len(password) - 6
				start_index = random.randint(0, max_index)
				easter = 'zając'
				new_password = ''
				for i in range(len(password)):
					if start_index <= i < start_index+5:
						new_password += easter[i - start_index]
					else:
						new_password += password[i]
				password = new_password

		self.ui.generatedpassword.setText(password)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MyForm()
	form.show()
	sys.exit(app.exec())
