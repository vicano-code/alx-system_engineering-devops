# A Puppet manifest that kills a process named killmenow.

exec { 'pkill_killmenow_process':
  command  => '/usr/bin/pkill -f /killmenow',
}

