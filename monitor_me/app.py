from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from flask_prometheus import monitor
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application Info', version='1.0.3')


@app.route("/")
@metrics.counter('invocation_by_type', 'hello()')
@metrics.gauge('in_progress', 'hello()')
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv("PORT"))  # Port where app will run from
