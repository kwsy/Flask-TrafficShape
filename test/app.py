# coding=utf-8
from flask import Flask
import hibiscus_traffic

app = Flask(__name__)


@app.route('/')
@hibiscus_traffic.tokenbucket(rate=2, default=5)
def hello_world():
    return 'Hello World!'


@app.route('/test')
@hibiscus_traffic.leakbucket(rate=3, default=20)
def hello():
    return 'hello test'


if __name__ == '__main__':
    app.run(port=8070, debug=True)
