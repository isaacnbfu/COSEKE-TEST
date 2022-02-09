from app import app
	from flaskext.mysql import MySQL
 
	mysql = MySQL()
 
	# MySQL configurations
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = '5555'
	app.config['MYSQL_DATABASE_DB'] = 'demo_DB'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	mysql.init_app(app)