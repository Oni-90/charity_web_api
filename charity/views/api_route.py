from flask import Blueprint, render_template
from charity.data import projets
from charity import charity_api

@charity_api.route('/')
def index():
    return render_template('index.html', projets = projets)