from flask import Flask

from api.HealthResource import HealthResource

app = Flask(__name__)

health = HealthResource(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)