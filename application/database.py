# -*- coding: utf-8 -*-

from PyQt4.QtSql import QSqlDatabase, QSqlQuery

class Database:
	def __init__(self):
		db = QSqlDatabase.addDatabase('QPSQL')
		db.setHostName('192.168.2.53')
		db.setDatabaseName('social_db')
		db.setUserName('social_admin')
		db.setPassword('admin00')

		if db.open():
			print "Conexion exitosa"
		else:
			print "No se puede conectar a PostgreSQL"

	def login(self, username, password):
		sql = 'SELECT username, password FROM users WHERE username=:username AND password=:password'
		q = QSqlQuery()
		q.prepare(sql)
		q.bindValue(':username', username)
		q.bindValue(':password', password)
		
		q.exec_()
		if q.next():
			print "Sesion correcta para %s" % username
			return True

	# CREATE TABLE
	# CREATE TABLE public.users (
	# 	id   integer   NOT NULL,
	# 	username   character varying(150),
	# 	password   character varying(150),
	# 	email   character varying(150),
	# 	first_name   character varying(200),
	# 	last_name   character varying(200)
	# )

	# INSERT TABLE
	# INSERT INTO public.users (
	# 	id,
	# 	username,
	# 	password,
	# 	email,
	# 	first_name,
	# 	last_name
	# ) values (1, 'eortiz', 'admin00', 'edgardo.ortiz.92@hotmail.com', 'Edgar', 'Ortiz')




