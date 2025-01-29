import os
import urllib.parse
import pandas as pd
import argparse
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Client Details
    band_name = request.args.get("band_name", "Band Name")
    client_name = request.args.get("client_name", "Client Name")
    client_email = request.args.get("client_email", "Client Email")
    client_phone = request.args.get("client_phone", "Client Phone")

    # Invoice Details
    invoice_number = request.args.get("invoice_number", "0001")
    date = request.args.get("date", "YYYY-MM-DD")
    payment_due = request.args.get("payment_due", "YYYY-MM-DD")

    # Items and total calculation
    items = []
    total_amount = 0

    # Extract item details from the URL query parameters
    item_names = request.args.getlist('item_name[]')
    quantities = request.args.getlist('quantity[]')
    prices = request.args.getlist('price[]')

    # Process the items and calculate totals
    for i in range(len(item_names)):
        item_name = item_names[i]
        quantity = int(quantities[i])
        price = float(prices[i])
        total = quantity * price
        items.append({"name": item_name, "quantity": quantity, "price": f"£{price:.2f}", "total": f"£{total:.2f}"})
        total_amount += total

    return render_template("invoice.html", 
                           band_name=band_name, 
                           client_name=client_name, 
                           client_email=client_email, 
                           client_phone=client_phone, 
                           invoice_number=invoice_number, 
                           date=date, 
                           payment_due=payment_due, 
                           items=items, 
                           total_amount=f"£{total_amount:.2f}")


def generate_urls_from_csv(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Loop through each row in the CSV and generate the URL
    for index, row in df.iterrows():
        # Extract data from the row
        band_name = row['band_name']
        client_name = row['client_name']
        client_email = row['client_email']
        client_phone = row['client_phone']
        invoice_number = row['invoice_number']
        date = row['date']
        payment_due = row['payment_due']

        # Extract item details
        items = []
        for i in range(1, 6):  # Assuming you have 5 items columns in the CSV
            item_name = row.get(f'item_name_{i}')
            quantity = row.get(f'quantity_{i}')
            price = row.get(f'price_{i}')
            if item_name and quantity and price:
                items.append({"name": item_name, "quantity": quantity, "price": price})

        # URL-encode the parameters
        band_name_encoded = urllib.parse.quote(band_name)
        client_name_encoded = urllib.parse.quote(client_name)
        client_email_encoded = urllib.parse.quote(client_email)
        client_phone_encoded = urllib.parse.quote(str(client_phone))
        invoice_number_encoded = urllib.parse.quote(str(invoice_number))
        date_encoded = urllib.parse.quote(date)
        payment_due_encoded = urllib.parse.quote(payment_due)

        # URL encode items
        item_data = []
        for item in items:
            item_data.append(f"item_name[]={urllib.parse.quote(item['name'])}")
            item_data.append(f"quantity[]={item['quantity']}")
            item_data.append(f"price[]={item['price']}")

        # Construct the URL with encoded parameters
        url = f"http://127.0.0.1:5000/?band_name={band_name_encoded}&client_name={client_name_encoded}&client_email={client_email_encoded}&client_phone={client_phone_encoded}&invoice_number={invoice_number_encoded}&date={date_encoded}&payment_due={payment_due_encoded}&" + "&".join(item_data)

        # Print the URL for each row in the CSV
        print(f"Generated URL: {url}")


if __name__ == "__main__":
    # Specify the path to your CSV file
    parser = argparse.ArgumentParser(description="Generate invoices from a CSV file.")
    parser.add_argument('csv_file', type=str, help="Path to the input CSV file")
    args = parser.parse_args()

    # Generate URLs from the provided CSV
    generate_urls_from_csv(args.csv_file)
    
    # Start the Flask app
    app.run(debug=False)
