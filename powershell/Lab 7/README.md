My script uses the Powershell package PackageManagement. With this you can find, download, install, and remove other Powershell packages.
My script shows you how to find, save instead of install, install, and if you want to, uninstall the package x7Zip.
In order for this script to run you will first need to run the command "Install-Module -Name PackageManagement" without the quotes.
If you just want to find the package x7Zip, uncomment line 1 by deleting the #, then run the script.
If you want to find and install the package x7Zip, uncomment lines 1 and 6, then run the script.
If you want to save the file instead of installing it, uncomment lines 3 and 4 (note you must have a C:\ drive for this to work) then run the script
Lastly, should you want to uninstall x7Zip, or the file you saved, or both, uncomment lines 8 and 9 and run the script. 
That is my demo of the PackageManager package for Powershell.
