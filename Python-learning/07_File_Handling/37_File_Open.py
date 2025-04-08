# Open a file for reading (default mode is 'rt' => read text)
f = open("Demofile.txt")

# Same as above, explicitly specifying read text mode
f = open("Demofile.txt", "rt")

# Open a file for appending in binary mode
f = open("Demofile", "ab")

# Open a file for writing text (overwrites if file exists)
f = open("Demofile.txt", "wt")

# Create a new file, fails if the file already exists
f = open("Newfile.txt", "xt")