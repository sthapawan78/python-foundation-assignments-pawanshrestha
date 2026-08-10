'''
Exercise: Dataset Comparison
Name: Pawan Shrestha
Day: 2'''

#Input values
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names
# Datasets found in both groups
# Datasets only in dataset_a
# Datasets only in dataset_b

#Calculations
all_unique_datasets=dataset_a.union(dataset_b)
common_datasets=dataset_a.intersection(dataset_b)
only_in_dataset_a=dataset_a.difference(dataset_b)
only_in_dataset_b=dataset_b.difference(dataset_a)

#Displaying the results
print(f"All Unique Datasets: {all_unique_datasets}")
print(f"Common Datasets: {common_datasets}")
print(f"Datasets only in Dataset A: {only_in_dataset_a}")
print(f"Datasets only in Dataset B: {only_in_dataset_b}")