from flask import Flask
from blueprints.team import team_blueprint
from blueprints.worker import worker_blueprint
from blueprints.task import task_blueprint
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(team_blueprint)
app.register_blueprint(task_blueprint)
app.register_blueprint(worker_blueprint)


