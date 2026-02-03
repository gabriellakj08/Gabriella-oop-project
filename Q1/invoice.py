class Invoice:
    def __init__(self, invoice_number, customer_name, issue_date):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.issue_date = issue_date

        self._items = []              # protected
        self.__total_amount = 0.0     # private

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, item_name, price):
        self._items.append((item_name, price))
        self.__total_amount += price

    def print_invoice(self):
        print("\n--- Invoice ---")
        print("Invoice Number:", self.invoice_number)
        print("Customer Name:", self.customer_name)
        print("Issue Date:", self.issue_date)
        print("Items:")
        for name, price in self._items:
            print(f"- {name}: {price}")
        print("Total Amount:", self.total_amount)
        print("--------------\n")
