from flask import Blueprint, render_template
from charity.data import projets
from charity import web_charity


@web_charity.route('/')
def index():
    return render_template('index.html', projets = projets)