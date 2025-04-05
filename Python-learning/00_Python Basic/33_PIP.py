# Check if PIP is installed
pip --version #cmd

#Download a package
pip install camelcase #Camelcase is a package

#Using a Package
import camelcase
c = camelcase.CamelCase()
txt = "Hello World!"
print(c.hump(txt))

#Remove/Uninstall a package
pip uninstall camelcase

#List Package
pip list 