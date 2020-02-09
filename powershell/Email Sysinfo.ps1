function getIP{
        (Get-NetIPAddress).ipv4address | Select-String "192*"
}
$IP = getIP
$User = $env:USERNAME
$Comp = $env:COMPUTERNAME
$Vers = $HOST.Version.Major
$Today = Get-Date -DisplayHint Date
$BODY = "This machine's IP is $IP. User is $User. Hostname is $Comp. Powershell version $Vers. Today's Date is $Today"
Send-MailMessage -To "Pickenjr@mail.uc.edu" -From "pickenjr@mail.uc.edu" -Subject "IT3038c Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)

