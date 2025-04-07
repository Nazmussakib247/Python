#Import the JSON module
import json

#Convert JSOn to python
#Some json
x = '{"name" : "Nazmus", "Age" : 23, "City" : "Khulna"}'
#parse x
y = json.loads(x)
#The result is python dictonary
print(y["Age"])

#Python to JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Converting Python objects into JSON strings, and printing the values
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Format result
json.dumps(x, indent=4)
#Using separator
json.dumps(x, indent=4, separators=(". ", " = "))

#Order the result
json.dumps(x, indent=4, sort_keys=True)