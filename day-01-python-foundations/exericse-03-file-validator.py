file_name = input("Enter a file name: ")

# Remove spaces and convert to lowercase
file_name = file_name.strip().lower()

if file_name.endswith(".csv"):
    print("Valid file: CSV")
elif file_name.endswith(".json"):
    print("Valid file: JSON")
elif file_name.endswith(".parquet"):
    print("Valid file: Parquet")
else:
    print("Invalid file format")