# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication
from application.login import LoginForm

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	login_form = LoginForm()
	login_form.show()

	with open('static/css/style.css', 'r') as static:
		theme = static.read()
	login_form.setStyleSheet(theme)
	sys.exit(app.exec_())
