# Open a File on the Server and read
f = open("Demofile.txt", "r")
print(f.read())

"""
# Open from a different location (Fixed path)
f = open(r"D:\Python\Python-learning\07_File_Handling\Demofile.txt", "r")
print(f.read())

Commenting for better run 
"""

#------------------->
#Read Only Parts of the File
#Return first 5 chracter of the file
f = open("Demofile.txt", "r")
print(f.read(5)) 

#Opening with 
with open("Demofile.txt", "r") as b:
    print(b.read())

#Read lines
#Read 1 line
f = open("demofile.txt", "r")
print(f.readline())

#Read 2 lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#Loop through the file line by line
f = open("Demofile.txt", "r")
for x in f:
    print(x)

#Close Files
f = open("Demofile.txt", "r")
print(f.readline())
f.close()
