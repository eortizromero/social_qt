# -*- coding: latin-1 -*-

from PyQt4.QtGui import QMainWindow, QWidget, QLabel
from PyQt4.QtCore import Qt

class LoginForm(QMainWindow):
	def __init__(self):
		super(LoginForm, self).__init__()
		self.width, self.height = 800, 650
		self.crear_interfaz(self.width, self.height)

	def crear_interfaz(self, width, height):
		self.setMinimumSize(width, height)
		self.setMaximumSize(width, height)
		self.setWindowTitle('Inicia sesión | SN')
		self.setObjectName('login_form_window')

		self.container = QWidget(self)
		self.container.setMinimumSize(width, height)
		self.container.setMaximumSize(width, height)
		self.container.setObjectName('login_container')

		self.title = QLabel(self)
		self.title.setText('I N I C I A  S E S I Ó N G R Á T I S')
		self.title.setGeometry(220, 150, 400, 40)
		self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.title.setObjectName('login_title')





