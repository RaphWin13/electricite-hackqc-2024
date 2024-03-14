from flask import Flask
from flask_cors import CORS

from api.HealthResource import HealthResource
from api.QuestionResource import QuestionResource
from api.FunFactResource import FunFactResource
from api.ScoreResource import ScoreResource

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:8080", "http://localhost:8080"]}})

health = HealthResource(app)
score = ScoreResource(app)
question = QuestionResource(app)
funfact = FunFactResource(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)