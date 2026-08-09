"""
Exercise: Sales Summary
Student: Pawan Shrestha
Day: 1
"""
#Input Values
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

#calculate gross sales
gross_sales = unit_price * quantity_sold

#calculate discount amount
discount_amount = gross_sales * discount_percentage

#calculate final sales amount
final_sales=gross_sales - discount_amount

#Displaying using f-string
print(f"Product: {product_name}")
print(f"Gross Sales: {gross_sales:.2f}")
print(f"Discount Amount: {discount_amount:.2f}")
print(f"Final Sales: {final_sales:.2f}")
