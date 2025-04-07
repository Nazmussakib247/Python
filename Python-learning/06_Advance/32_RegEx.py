import json

# Python dict → JSON string
person = {
  "name": "Sakib",
  "age": 22,
  "city": "Dhaka"
}
json_string = json.dumps(person)
print("Python to JSON string:")
print(json_string)

# JSON string → Python dict
json_data = '{"name": "Sakib", "age": 22, "city": "Dhaka"}'
python_dict = json.loads(json_data)
print("\nJSON string to Python dictionary:")
print(python_dict)
print("Access name:", python_dict["name"])

# Other Python objects to JSON
print("\nPython list to JSON:", json.dumps(["apple", "banana"]))
print("Python tuple to JSON:", json.dumps(("apple", "banana")))
print("Python int to JSON:", json.dumps(23))
print("Python boolean to JSON:", json.dumps(True))

# JSON string with formatting
data = {
  "name": "Sakib",
  "age": 22,
  "hobbies": ["coding", "reading", "gaming"],
  "is_student": True,
  "address": {"city": "Dhaka", "zip": "1207"}
}
print("\nFormatted JSON string:")
print(json.dumps(data, indent=4))

# Write JSON to file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
print("\n✅ JSON data written to output.json")

# Read JSON from file
with open("output.json", "r") as file:
    loaded_data = json.load(file)
    print("\nRead data from output.json:")
    print(loaded_data)
    print("City:", loaded_data["address"]["city"])