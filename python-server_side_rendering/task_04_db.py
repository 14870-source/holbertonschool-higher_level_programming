#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json():
    """Read products from a JSON file."""
    file_path = os.path.join(BASE_DIR, 'products.json')

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from a CSV file."""
    file_path = os.path.join(BASE_DIR, 'products.csv')

    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from the SQLite database."""
    db_path = os.path.join(BASE_DIR, 'products.db')

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = [dict(row) for row in cursor.fetchall()]
        return products
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template(
                'product_display.html',
                products=[],
                error='Wrong source'
            )

        if product_id is not None:
            data = [
                product for product in data
                if str(product.get('id')) == product_id
            ]

            if not data:
                return render_template(
                    'product_display.html',
                    products=[],
                    error='Product not found'
                )

        return render_template(
            'product_display.html',
            products=data,
            error=None
        )

    except (sqlite3.Error, OSError, json.JSONDecodeError) as error:
        return render_template(
            'product_display.html',
            products=[],
            error=f'Data error: {error}'
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)