# from app import app
from app_testing import app

if __name__ == '__main__':
	app.run(port = 8001, debug = True)