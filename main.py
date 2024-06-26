import random
import string
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.generate.clicked.connect(self.generate)
		self.ui.easter.clicked.connect(self.easterClicked)
		self.ui.password.textChanged.connect(self.checkStrongPassword)

		self.smallChars = [l for l in string.ascii_lowercase]
		self.capitalChars = [l for l in string.ascii_uppercase]
		self.numbers = [str(i) for i in range(0, 10)]
		self.specialChars = [l for l in string.punctuation]



	def generate(self):

			length = int(self.ui.passwordLength.text())
			password_type = self.ui.passwordType.currentText()
			password = ''
			counter = 0

			if password_type == 'Pin':
				for i in range(length):
					password += str(random.randint(0, 9))
			elif self.ui.word.isChecked():
				words = self.readDict('odm.txt')
				while len(password) < int(length):
					password += random.choice(words)
			else:
				while True:
					elements = []
					elements.append(self.smallChars)
					if self.ui.capitalChars.isChecked():
						counter += 1
						elements.append(self.capitalChars)
					if self.ui.numbers.isChecked():
						counter += 1
						elements.append(self.numbers)
					if self.ui.specialChar.isChecked():
						counter += 1
						elements.append(self.specialChars)

					if int(length) <= counter:
						print("Za mało")
						return

					for i in range(length):
						element_type = random.choice(elements)
						password += random.choice(element_type)

					if self.check_password(password):
						self.ui.genertedPassword.setText(password)
						break

			if self.ui.easter.isChecked() and len(password) >= 5:
				max_index = len(password) - 6
				start_index = random.randint(0, max_index)
				new_password = ''
				easter = 'zając'
				for i in range(len(password)):
					if start_index <= i < start_index + 5:
						new_password += easter[i - start_index]
					else:
						new_password += password[i]
				password = new_password

	def checkStrongPassword(self):
		suma =0
		password = self.ui.password.text()
		for i in range(len(password)):
			suma = suma + i
			self.ui.passwordPower.setValue(suma)


	def check_password(self, password):
		if not any(char.islower() for char in password):
			return False
		if self.ui.capitalChars.isChecked() and not any(char.isupper() for char in password):
			return False
		if self.ui.numbers.isChecked() and not any(char.isdigit() for char in password):
			return False
		if self.ui.specialChar.isChecked() and not any(char in string.punctuation for char in password):
			return False
		return True

	def easterClicked(self):
		if self.ui.easter.isChecked():
			self.ui.numbers.setChecked(False)
			self.ui.capitalChars.setChecked(False)
			self.ui.specialChar.setChecked(False)
			self.ui.word.setChecked(False)
			self.ui.numbers.setDisabled(True)
			self.ui.capitalChars.setDisabled(True)
			self.ui.specialChar.setDisabled(True)
			self.ui.word.setDisabled(True)
		else:
			self.ui.numbers.setDisabled(False)
			self.ui.capitalChars.setDisabled(False)
			self.ui.specialChar.setDisabled(False)
			self.ui.word.setDisabled(False)

	def readDict(self, path):
		words = []
		with open(path, 'r', encoding='utf-8') as file:
			lines = file.readline()
			for line in file:
				line = lines.split(',')[0]
				line = line.replace('\n','')
				if(len(line) > 2 and line.find(' ') == -1):
					words.append(line)
			return words

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MyForm()
	form.show()
	sys.exit(app.exec())