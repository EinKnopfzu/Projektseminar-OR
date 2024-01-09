from flask import jsonify, Flask, request
from datenesel import generate_product_features
from datenesel import refine_product_features
from openai_requests import openai_requests

def create_routes(app):

    @app.errorhandler(404)
    def invalid_route(e):
        return "Invalid route..."

    @app.route('/generate', methods = ['POST'])
    def generate_output():
        config = request.json

        datenesel = refine_product_features(generate_product_features(config))
        return openai_requests(datenesel, config)

