"""
Exercise: Data Quality Checker
Student: Pawan Shrestha
Day: 1
"""
#Input Values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

#Calculate the total number and percentage of problematic rows.
problematic_rows=missing_rows + duplicate_rows
problematic_rows_percentage=(problematic_rows / total_rows) * 100

if problematic_rows_percentage < 2:
    final_classification="Excellent"
elif problematic_rows_percentage < 5:
    final_classification="Acceptable"
else:
    final_classification="Needs Cleaning"

#Displaying the results
print(f"Total Rows: {total_rows}")
print(f"Problematic Rows: {problematic_rows}")
print(f"Problematic Rows Percentage: {problematic_rows_percentage:.2f}%")
print(f"Final Classification: {final_classification}")