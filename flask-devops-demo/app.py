from flask import Flask, jsonify
import logging
from logging.handlers import RotatingFileHandler
import datetime

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/health')
def health_check():
    app.logger.info('Health check endpoint accessed')
    return jsonify({"status": "healthy"})

@app.route('/api/v1/hello')
def hello():
    app.logger.info('Hello endpoint accessed')
    return jsonify({"message": "Hello, World!"})

@app.route('/api/v1/version')
def version():
    app.logger.info('Version endpoint accessed')
    return jsonify({
        "version": "1.0.0",
        "environment": "production",
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.logger.info('Application startup')
    app.run(host='0.0.0.0', port=5000)
