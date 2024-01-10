from flask import jsonify, Flask, request
from datenesel import generate_product_features
from datenesel import refine_product_features
from openai_requests import openai_requests
import logging
from threading import Lock

status_global = "backend started"

def create_routes(app):

    @app.errorhandler(404)
    def invalid_route(e):
        logging.warning('Invalid route...')
        return "Invalid route..."

    @app.route('/generate', methods = ['POST'])
    def generate_output():
        config = request.json
        logging.info('Post-Config: ' + str(config))

        datenesel = refine_product_features(generate_product_features(config))
        return openai_requests(datenesel, config)

    data_lock = Lock()
    @app.route('/status')
    def get_data():
        with data_lock:
            global status_global
            return jsonify({"status": status_global})


