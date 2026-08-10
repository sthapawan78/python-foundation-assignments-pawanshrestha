'''
Exercise: Batch Processor
Name: Pawan Shrestha
Day: 2
'''
for batch_number in range(1,10):
    print(f"Processing Batch {batch_number}")
    if batch_number %3==0:
        print("Checkpoint reached")

