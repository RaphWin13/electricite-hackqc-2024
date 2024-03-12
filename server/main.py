from flask import Flask

from api.HealthResource import HealthResource
from api.QuestionResource import QuestionResource

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8080"}})

health = HealthResource(app)
question = QuestionResource(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)