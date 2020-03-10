$Machines = 'PICKENJR-WIN'
Foreach($Machine in $Machines) {
    $RCounters = Get-Counter -ListSet * -ComputerName $Machine
    write-host("there are {0} counters on {1}" -f $RCounters.count, ($Machine)) 
} 