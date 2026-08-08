rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

# Calculate failure rate
failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100

# Determine pipeline status
if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate > 5:
    status = "Critical"
elif failure_rate > 2:
    status = "Warning"
else:
    status = "Warning"

print("Failure Rate:", failure_rate, "%")
print("Pipeline Status:", status)