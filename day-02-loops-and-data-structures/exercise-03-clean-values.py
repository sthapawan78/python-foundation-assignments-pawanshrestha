'''
Exercise : Clean Values
Name: Pawan Shrestha
Day: 2
'''
 #Input values
raw_values = [100, None, 250, "invalid", 300, "pawan", None, 450, 500, "dlytica", 600]
cleaned_values = []

#Loop through the raw values and clean them
for value in raw_values:
    if  not isinstance(value,int):  #Check if the value is an integer
        continue  #Skip the invalid value and continue to the next iteration
    cleaned_values.append(value) #Add the valid integer value to the cleaned_values list
   
#Print the cleaned values
print("Cleaned Values:", cleaned_values)  
print(f"Cleaned Values: {cleaned_values}")

#same process through list comprehension
cleaned_values_lc = [value for value in raw_values if isinstance(value, int)]
print(f"Cleaned Values using List Comprehension: {cleaned_values_lc}")