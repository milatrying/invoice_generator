import os
import urllib.parse
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Client Details
    client_company_name = request.args.get("client_company_name", "Client Company Name")
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
                           client_company_name=client_company_name, 
                           client_name=client_name, 
                           client_email=client_email, 
                           client_phone=client_phone, 
                           invoice_number=invoice_number, 
                           date=date, 
                           payment_due=payment_due, 
                           items=items, 
                           total_amount=f"£{total_amount:.2f}")


def get_input():
    print("Enter client details:")
    client_company_name = input("Client Company Name: ")
    client_name = input("Client Name: ")
    client_email = input("Client Email: ")
    client_phone = input("Client Phone: ")

    print("Enter invoice details:")
    invoice_number = input("Invoice Number: ")
    date = input("Date (YYYY-MM-DD): ")
    payment_due = input("Payment Due Date (YYYY-MM-DD): ")

    # Get the item details from the user
    items = []
    while True:
        print("\nEnter item details:")
        item_name = input("Item Name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Quantity for {item_name}: "))
        price = float(input(f"Price for {item_name}: £"))
        items.append({"name": item_name, "quantity": quantity, "price": price})
    
    # URL-encode the parameters
    client_company_name_encoded = urllib.parse.quote(client_company_name)
    client_name_encoded = urllib.parse.quote(client_name)
    client_email_encoded = urllib.parse.quote(client_email)
    client_phone_encoded = urllib.parse.quote(client_phone)
    invoice_number_encoded = urllib.parse.quote(invoice_number)
    date_encoded = urllib.parse.quote(date)
    payment_due_encoded = urllib.parse.quote(payment_due)

    # URL encode items
    item_data = []
    for item in items:
        item_data.append(f"item_name[]={urllib.parse.quote(item['name'])}")
        item_data.append(f"quantity[]={item['quantity']}")
        item_data.append(f"price[]={item['price']}")

    # Construct the URL with encoded parameters
    url = f"http://127.0.0.1:5000/?client_company_name={client_company_name_encoded}&client_name={client_name_encoded}&client_email={client_email_encoded}&client_phone={client_phone_encoded}&invoice_number={invoice_number_encoded}&date={date_encoded}&payment_due={payment_due_encoded}&" + "&".join(item_data)

    print("\nOpen the following URL in your browser:")
    print(url)

    return url


if __name__ == "__main__":
    # Get input and generate the URL
    get_input()
    
    # Start the Flask app
    app.run(debug=False)
