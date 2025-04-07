#Set-Unordered, unchangeable*, unindexed
#Create a set
myset = {"Apple", "Orange", "Pineaple", "Jackfruit"}
print(myset)

# (1,True)-(0,False) considered as same value
thisset = {"apple", "banana", "cherry", False, True, 0, 1}
print(thisset)

#Length of a set
print(len(thisset))

#Data type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() constructor
thisset = set(("apple", "banana", "cherry", False, True, 0, 1))
print(thisset)

