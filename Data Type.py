a = str('Hello world!')

b = int(20)
c = float(20.5)
d = complex(20j)

e = list(("apple", "Orange", "Banana"))
# List is mutabble/changeable & slow[]

f = tuple(("Apple", "Cherry", "Mangoes"))
#Tuple is immutable & fast

g = range(100)
h = dict(name='John', age = 40)

i = set(("Apple","Malta", "Guava"))
#Mutable unordered collection of unique elements{}
j = frozenset(("Malta", "Grape", "Litchi"))
# Unmuteable version of set

k = bool(5)
#True-false
l = bytes(10)
#Immuteable version of byte 0-255
m = bytearray(20)
#muteable version of byte

n = memoryview(bytes(11))
#Ascessing or slicing binary data without copying it
