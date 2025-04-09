from flask import Flask, jsonify
import logging
import os
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

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask DevOps Demo!"})

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
