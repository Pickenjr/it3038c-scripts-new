#This script displays the used and free space of all drives on the system
#Line 4 assigns a variable gets our drive information, Line 5 displays the Device ID which tells us which drive is which, 
#Lines 6 and 7 format the output of the used and free space and the header for them to show it's in GB  
Get-WmiObject -Class win32_logicaldisk | 
Select-Object DeviceId, 
@{n="Size(GB)";e={[math]::Truncate($_.Size/1GB)}},
@{n="Free Space(GB)";e={[math]::Truncate($_.FreeSpace/1GB)}}