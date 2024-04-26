import flask
from flask_cors import CORS
from charity import web_charity, charity_api
from extensions import db
from charity.models.projet import Projet

app = flask.Flask(__name__)


from flask_migrate import Migrate

CORS(app, origins="*")

app.register_blueprint(web_charity, url_prefix='/charity')
app.register_blueprint(charity_api, url_prefix='/api/charity')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:maxwell2004@localhost/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

# with app.app_context():
#     db.create_all()