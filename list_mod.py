"""Simulate impression service"""


def print_models(orders, printed):
    """simulate the printing of the orders list"""

    while orders:
        current_model = orders.pop()
        print(f"currently printing: {current_model}")
        printed.append(current_model)


def show_completed(completed):
    """Show the printed orders"""
    print("These are the orders already printed:")
    for printed in completed_models:
        print(printed)


current_orders = ["gunda", "wing", "gunpla"]
completed_models = []

print_models(current_orders, completed_models)
show_completed(completed_models)
