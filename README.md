# Invoice Generator

A Python-based application designed to streamline the creation of professional invoices with ease.
Within this repo there are two approaches to creating invoices:
1. One at a time, using inputs via the terminal
2. Bulk using a csv (template found [here](input.csv)

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage)
- [PDF Export](#PDF-Export)



## Installation

To set up the Invoice Generator locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/milatrying/invoice_generator.git
   cd invoice_generator

2. **Set up your details in the template**:
   In the [invoice.html](/templates/invoice.html), you will see sections where you can fill in your company information and payment information.

## Usage
### Individual invoice generator
This script allows you to create 1 invoice at a time, based on user inputs from the terminal. 
To execute do the following:
```python
  python invoice_generator.py
```

Once you run this command in the terminal (having navigated to the folder location), you will be prompted to input the details about the client, invoice & items. 
<details>
  <summary>Example of what the input would look like in the terminal</summary>
  
```bash
> Enter client details:
Client Company Name: Test
Client Name: Test
Client Email: Test@gmail.com
Client Phone: 123456570
> Enter invoice details:
Invoice Number: 1
Date (YYYY-MM-DD): 2025-02-02
Payment Due Date (YYYY-MM-DD): 2025-02-02

> Enter item details:
Item Name (or type 'done' to finish): Test1
Quantity for Test1: 1
Price for Test1: £10

> Enter item details:
Item Name (or type 'done' to finish): Test2
Quantity for Test2: 2
Price for Test2: £5

Enter item details:
Item Name (or type 'done' to finish): done
```
</details>

ℹ️ When providing quantity or price for the invoice items, please make sure these are numeric as this will affect the subtotal/total calculations

### Bulk invoice generator
This script takes a csv with details about the invoices you want to create and loops through them. 
The invoices are then generated as separate links in the terminal, which you can click to visit and then save as pdf files. 
To execute this script:
```python
  python invoice_generator_bulk.py input.csv
```

ℹ️ The `input.csv` can be stored anywhere on your local system, you would just need to pass the full path to the file to correctly point to it. 


## PDF Export
Once the html has been generated, you can save the html as a pdf using the browsers `print` functionality. 
* [Chrome](https://www.greengeeks.com/tutorials/save-a-web-page-as-a-pdf-in-chrome-browser/)


