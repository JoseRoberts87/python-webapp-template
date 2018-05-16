from flask_api import FlaskAPI
import sqlalchemy as sa

app = FlaskAPI(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
