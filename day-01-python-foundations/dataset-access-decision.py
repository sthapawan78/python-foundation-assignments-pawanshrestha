"""
Exercise: Dataset Access Decision
Student: Pawan Shrestha
Day: 1
"""

#Input variables
user_role="scientist"
is_active=False
requested_dataset="customer_data"

allowed_roles=["analyst","scientist","engineer"]

restricted_datasets=["salary_data","personal_data"]


if user_role in allowed_roles and is_active and requested_dataset not in restricted_datasets:
    print("Access granted to the dataset.")
else:
    if user_role not in allowed_roles:
        print("Access denied because the role is not allowed.")
    if not is_active:
        print("Access denied because the user is inactive.")
    if requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    