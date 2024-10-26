class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []  # Initialize items as an empty list
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        '''Adds an item to the cash register.'''
        self.last_transaction = price * quantity  # Store the last transaction amount
        self.total += self.last_transaction  # Update total
        self.items.extend([title] * quantity)  # Add item title(s) to the items list

    def apply_discount(self):
        '''Applies a discount to the total and returns the new total.'''
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}"
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        '''Reverts the last transaction from the total.'''
        self.total -= self.last_transaction
        # Update the items list to reflect the last transaction
        # We need to figure out how to remove the last item(s) added
        if self.last_transaction > 0:
            for item in self.items[-1:]:  # Get the last item title
                if item and self.last_transaction > 0:
                    self.items.remove(item)  # Remove the last item
                    self.last_transaction = 0.0  # Reset last transaction
                    break  # Exit after removing one item
