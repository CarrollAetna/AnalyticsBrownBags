from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Healthcheck to ensure service is running
    """
    logger.info("Service healthy!")
    return "Service healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)