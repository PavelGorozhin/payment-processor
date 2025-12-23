import os
import logging
from flask import Flask, request, jsonify
from payment_processor.services.payment import PaymentService

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
config = os.environ.get('PAYMENT_PROCESSOR_CONFIG', 'default_config.py')
app.config.from_pyfile(config)

# Initialize payment service
payment_service = PaymentService(app.config['PAYMENT_SERVICE_URL'])

@app.route('/process_payment', methods=['POST'])
def process_payment():
    try:
        data = request.get_json()
        payment_result = payment_service.process_payment(data['amount'], data['currency'])
        return jsonify(payment_result)
    except Exception as e:
        logger.error(f'Error processing payment: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)