My script uses the Powershell package PackageManagement. With this you can find, download, install, and remove other Powershell packages.
My script shows you how to find, save instead of install, install, and if you want to, uninstall the package x7Zip.
In order for this script to run you will first need to run the command "Install-Module -Name PackageManagement" without the quotes.

If you just want to find the package x7Zip then uncomment line 1 and run the script, or enter the following command

```bash
Find-Package x7Zip
```

If you want to find and install the package x7Zip, uncomment lines 1 and 6, then run the script, or enter the following command.

```bash
Install-Package x7Zip
```

If you want to save the file instead of installing it, uncomment lines 3 and 4 (note you must have a C:\ drive for this to work) then run the script, or run the following two commands

```bash
Mkdir C:\x7Zip
Save-Package x7Zip -Path C:\x7Zip
```

Lastly, should you want to uninstall x7Zip, or the file you saved, or both, uncomment lines 8 and 9 and run the script or run the following 2 commands. 

```bash
Remove-Item C:\x7Zip -Force
Uninstall-Package x7Zip
```

That is my demo of the PackageManager package for Powershell.
