'''
Exercise : Sales Analysis
Name: Pawan Shrestha
Day: 2'''
#Input values
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

#Caluclation
sorted_sales =[value for value in sorted(monthly_sales, reverse=True)] #sorting the sales in descending order using list comprehension

high_sales= [value for value in monthly_sales if value >100000] #filtering the sales > 100000

vat_added_sales = [value * 1.13 for value in monthly_sales] #adding 13% VAT to the sales
formatted_vat_added_sales = [f"{value:.2f}" for value in vat_added_sales] #formatting the VAT added sales to 2 decimal places

total_sales =sum(monthly_sales) #calculating the total sales

average_sales = total_sales / len(monthly_sales)    #calculating the average sales

#Displaying the results
print(f"Sorted Sales: {sorted_sales}" )
print(f"High Sales: {high_sales}" )
print(f"VAT Added Sales: {formatted_vat_added_sales}" )
print(f"Total Sales Amount: {total_sales}" )
print(f"Average Sales Amount: {average_sales}" )