from flask import  Blueprint
# from flask import Blueprint, jsonify
# from charity.data import  projets

web_charity = Blueprint ('charity_web', __name__, template_folder='templates', static_folder='static')
charity_api = Blueprint('charity_api', __name__, template_folder='templates', static_folder='static')

from charity.views import route, api_route
