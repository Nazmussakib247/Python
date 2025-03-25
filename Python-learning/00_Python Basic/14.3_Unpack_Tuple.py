fruits =("apple", "banana", "Cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)