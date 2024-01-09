from flask import Flask
from routes import create_routes
from remove_old_logs import remove_old_logs
import logging
import datetime


def main():

    remove_old_logs()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logging.basicConfig(filename=f"logs\\myapp_{current_time}.log", level=logging.INFO)

    app = Flask(__name__)

    create_routes(app)
    app.run(debug=True)
    logging.info('Flaskserver gestartet')



if __name__ == '__main__':
    main()
