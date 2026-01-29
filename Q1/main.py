from invoice import Invoice

def main():
    
    invoice_number = input("Enter invoice number: ")
    customer_name = input("Enter customer name: ")
    issue_date = input("Enter issue date: ")

    
    inv = Invoice(invoice_number, customer_name, issue_date)

    
    item_name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    inv.add_item(item_name, price)

    inv.print_invoice()

if __name__ == "__main__":
    main()
