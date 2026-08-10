'''
Exercise: Retry Simulation
Name: Pawan Shrestha
Day: 2
'''

#Input Variable
attempt = 1
max_attempts = 3
operation_successful = False

#Retry simulation loop
while attempt <= max_attempts:
    print(f"Attempt {attempt}")
    
    if attempt == 2:
        operation_successful = True # Simulating a successful operation on the second attempt
        break 
    attempt += 1
if operation_successful:
        print("Operation successful!")
else:
        print("Operation failed after maximum attempts.")
