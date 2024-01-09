from flask import Flask
from routes import create_routes

def main():
    app = Flask(__name__)
    create_routes(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()
