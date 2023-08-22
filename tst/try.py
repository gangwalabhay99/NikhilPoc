import json

# The provided JSON data
json_data = "C:\Users\agangwal\OneDrive - Insight\Desktop\pipeline github\nikhilPoc\test.json"
# Parse the JSON data
data = json.loads(json_data)
print(json_data)

# # Access the controls results
# controls_results = data.get("profiles")[0].get("controls")[0].get("results")

# # Count the number of "passed" statuses
# passed_count = sum(1 for result in controls_results if result.get("status") == "passed")

# print("Number of 'passed' statuses:", passed_count)
