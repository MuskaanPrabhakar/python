#Build a shopping cart using a list of tuples (item_name, price, quantity). Write functions to compute total price, apply a discount if total exceeds 1000, and print an itemized receipt with formatted output.
# Shopping cart: (item_name, price, quantity)
cart = [
    ("Laptop Bag", 750, 1),
    ("Mouse", 250, 2),
    ("Keyboard", 600, 1)
]
def compute_total(cart):
    total = sum(t[1]*t[2] for t in cart)
    return total
def apply_discount(total):
    discount = total*0.10
    return total - discount, discount
def print_receipt(cart):
    print("=" *50)
    print("SHOPPING RECEIPT")
    print("=" * 50)
    print("")
    print("-" * 50)
    print(f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}")
    print("-" * 50)
    for item, price, quantity in cart:
        subtotal = price * quantity
        print(f"{item:<20} {price:<10} {quantity:<10} {subtotal:<10}")
    total = compute_total(cart)
    final_total, discount = apply_discount(total)
    print("-" * 50)
    print(f"Your total is: {total}")
    print("-" * 50)
    if discount > 0:
        print(f"For purchasing more than 1000, we offer you {discount} discount of 10 percent")
    print("=" * 50)
    print(f"Pay this {final_total} via cash or QR code")
    print("=" * 50)
    print("HAPPY SHOPPING")

print_receipt(cart)