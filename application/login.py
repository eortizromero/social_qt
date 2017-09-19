# -*- coding: latin-1 -*-

from PyQt4.QtGui import QMainWindow, QWidget, QLabel, QLineEdit, QCheckBox, QCursor, QPushButton
from PyQt4.QtCore import Qt, QPropertyAnimation, QRect, QEvent, QTimer
from database import Database

from PyQt4 import QtGui

class LoginForm(QMainWindow):
	def __init__(self, parent=None):
		super(LoginForm, self).__init__(parent)
		self.width, self.height = 800, 650
		self.crear_interfaz(self.width, self.height)
		self.checkbox_rememberme.clicked.connect(self.remember_me)
		self.button_login.clicked.connect(self.logging)
		# self.div_create.setVisible(False)
		self.database = Database()
		"""self.label_rememberme.mousePressEvent = self.do_remember

	def do_remember(self, event):
		# TDE FIXME: Create another remember_me method for remember me label 
		self.remember_me(event)
		"""
	def loading(self):
		print "loading..."

	def logging(self):
		self.valid_fields()
		
	def valid_fields(self):
		username = self.username.text()
		password = self.password.text()
		
		if username == '':
			self.username.setFocus(True)
		elif password == '':
			self.password.setFocus(True)
		else:
			self.loading()
			self.username.setEnabled(False)
			self.password.setEnabled(False)
			print "Logging validation username"
			if self.database.login(username, password):
				print "Bienvenido %s" % username
			else:
				print "Datos incorrectos!"

		# return True in end of statement

	def anim_left(self):
		animation = QPropertyAnimation(self.label_icon, "geometry")
		animation.setDuration(250)
		animation.setStartValue(QRect(0, 0, 20, 20))
		animation.setEndValue(QRect(20, 0, 20, 20))
		animation.start()
		self.animation = animation

	def anim_right(self):
		animation = QPropertyAnimation(self.label_icon, "geometry")
		animation.setDuration(250)
		animation.setStartValue(QRect(20, 0, 20, 20))
		animation.setEndValue(QRect(0, 0, 20, 20))
		animation.start()
		self.animation = animation

	def remember_me(self):
		if self.checkbox_rememberme.isChecked():
			self.anim_left()
			self.label_icon.setGeometry(20, 0, 20, 20)
		else:
			self.anim_right()
			self.label_icon.setGeometry(0, 0, 20, 20)

	def crear_interfaz(self, width, height):
		self.setMinimumSize(width, height)
		self.setMaximumSize(width, height)
		self.setWindowTitle('I n i c i a  s e s i � n | SN')
		self.setObjectName('login_form_window')

		self.container = QWidget(self)
		self.container.setMinimumSize(width, height)
		self.container.setMaximumSize(width, height)
		self.container.setObjectName('login_container')

		self.title = QLabel(self)
		self.title.setText('I N I C I A   S E S I � N   G R � T I S')
		self.title.setGeometry(210, 130, 400, 40)
		self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.title.setObjectName('login_title')

		self.username = QLineEdit(self)
		self.username.setPlaceholderText('N O M B R E  D E  U S U A R I O')
		self.username.setGeometry(260, 230, 300, 40)
		self.username.setObjectName('login_username')
		self.username.setAcceptDrops(False)

		self.password = QLineEdit(self)
		self.password.setPlaceholderText('C O N T R A S E � A')
		self.password.setGeometry(260, 290, 300, 40)
		self.password.setObjectName('login_password')
		self.password.setEchoMode(QLineEdit.Password)

		self.checkbox_rememberme = QCheckBox(self)
		self.checkbox_rememberme.setLayoutDirection(Qt.RightToLeft)
		self.checkbox_rememberme.setGeometry(260, 360, 40, 20)
		self.checkbox_rememberme.setObjectName("login_rememberme")
		self.checkbox_rememberme.setCursor(QCursor(Qt.PointingHandCursor))

		self.label_icon = QLabel(self.checkbox_rememberme)
		self.label_icon.setGeometry(0, 0, 20, 20)
		self.label_icon.setObjectName("label_icon")

		self.label_rememberme = QLabel(self)
		self.label_rememberme.setText("R E C U � R D A M E")
		self.label_rememberme.setGeometry(310, 360, 165, 20)
		self.label_rememberme.setObjectName("label_rememberme")

		self.button_login = QPushButton(self)
		self.button_login.setGeometry(315, 420, 200, 40)
		self.button_login.setText("I N I C I A R  S E S I � N")
		self.button_login.setObjectName("button_login")

		self.layout = QGridLayout(self.container)

		# self.div_create = QWidget(self)
		# self.div_create.setMinimumSize(300, 40)
		# self.div_create.setMaximumSize(300, 40)
		# self.div_create.setGeometry(200, 180, 300, 40)
		# self.div_create.setObjectName('div_create')




