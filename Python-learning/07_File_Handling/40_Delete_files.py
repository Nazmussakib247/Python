#Delete file
import os
os.remove("Demofile.txt")

#Check if File exist
import os
if os.path.exists("Demofile.txt"):
    os.remove("Demofile.txt")
else:
    print("The file does not exist")

#Delete folder
import os
os.rmdir("Myfolder")