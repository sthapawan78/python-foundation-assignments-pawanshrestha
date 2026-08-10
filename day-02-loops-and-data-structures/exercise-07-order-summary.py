'''
Exercise : Order Summary
Name: Pawan Shrestha
Day: 2'''

#Input values
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Pending"
    }
}
# Print every order ID and customer.
# Print only completed orders.
# Calculate the total amount of completed orders.
# Count pending orders.
# Add a new order to the dictionary

#Calculations
# Print every order ID and customer.
for order_id, order_details in orders.items():
    print(f"Order ID: {order_id}, Customer: {order_details['customer']}")

# Print only completed orders.
completed_orders={order_id: order_details for order_id, order_details in orders.items() if order_details['status']=="Completed"}
for order_id, order_details in completed_orders.items():
    print(f"Completed Order ID: {order_id}, Customer: {order_details['customer']}, Amount: {order_details['amount']}")

# Calculate the total amount of completed orders.
total_completed_amount=sum(order_details['amount'] for order_details in completed_orders.values())
print(f"Total Amount of Completed Orders: {total_completed_amount}")

# Count pending orders.
pending_orders_count=sum(1 for order_details in orders.values() if order_details['status']=="Pending")
print(f"Number of Pending Orders: {pending_orders_count}")

# Add a new order to the dictionary
new_order_id = "ORD-004"
new_order_details = {
    "customer": "Sita",
    "amount": 1500,
    "status": "Pending"
}
orders[new_order_id] = new_order_details
print(orders)

