#! /usr/bin/env python3.6
import os
from flask import Flask, request

import stripe
# This test secret API key is a placeholder. Don't include personal details in requests with this key.
# To see your test secret API key embedded in code samples, sign in to your Stripe account.
# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:5173'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    line_items = request.json['line_items']
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
    except Exception as e:
        print(str(e))
        return str(e)

    return {'url': checkout_session.url}

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    product = stripe.Product.create(
        name=data['name'],
    )

    price = stripe.Price.create(
        unit_amount=data['price'] * 100,
        currency='RON',
        product=product.id,
    )
    
    return {'price_id': price.id}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
