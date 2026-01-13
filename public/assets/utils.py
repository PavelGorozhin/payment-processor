# utils.py

import logging
import datetime

from payment_processor.config import config

logger = logging.getLogger(__name__)

def get_current_timestamp():
    """Return the current timestamp in seconds."""
    return int(datetime.datetime.now().timestamp())

def format_currency(amount):
    """Format a currency amount with two decimal places."""
    return f"${amount:.2f}"

def validate_card_number(card_number):
    """Validate a credit card number using the Luhn algorithm."""
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    for d in even_digits:
        checksum += sum(digits_of(d))
    for d in odd_digits:
        checksum += sum(digits_of(d) * 2) % 10
    return checksum % 10 == 0

def is_valid_payment_method(payment_method):
    """Check if a payment method is valid."""
    return payment_method in config.VALID_PAYMENT_METHODS