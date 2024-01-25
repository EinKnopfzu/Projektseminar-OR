from flask import jsonify, Flask, request
from datenesel import generate_product_features
from datenesel import refine_product_features
from openai_requests import openai_requests
from reprompt import reprompt_request
import logging
from threading import Lock


status_global =  {
        "Daten vorverarbeitet" : False,
        "Daten vorabgefragt": False,
        "Datenesel erstellt": False,
        "Hauptabfrage AmazonTitle": False,
        "Antwort AmazonTitle": False,
        "Hauptabfrage DescriptionLongShops": False,
        "Datenähnlichkeiten gestartet" : False,
        "Datenähnlichkeiten abgeschlossen" : False,
        "Antwort DescriptionLongShops": False,
        "Hauptabfrage SalesArguments": False,
        "Antwort SalesArguments": False,
        "Hauptabfrage AmazonBulletPoints": False,
        "Antwort AmazonBulletPoints": False,
        "Hauptabfrage WorthKnowingShop": False,
        "Antwort WorthKnowingShop": False,
        "Hauptabfrage MetaKeywordShop": False,
        "Antwort MetaKeywordShop": False,
        "Hauptabfrage Reprompt": False,
        "Antwort Reprompt": False
    }

def create_routes(app):

    @app.errorhandler(404)
    def invalid_route(e):
        logging.warning('Invalid route...')
        return "Invalid route..."

    @app.route('/generate', methods = ['POST'])
    def generate():
        config = request.json
        logging.info('Generate-Config: ' + str(config))

        generate_res = generate_product_features(config)
        datenesel = refine_product_features(generate_res["output"], generate_res["input"])
        return openai_requests(datenesel, config)

    @app.route('/reprompt', methods=['POST'])
    def reprompt():
        reprompt_config = request.json
        logging.info('Reprompt-Config: ' + str(reprompt_config))

        return reprompt_request(reprompt_config)

    data_lock = Lock()
    @app.route('/status')
    def get_data():
        with data_lock:
            global status_global
            return jsonify(status_global)


