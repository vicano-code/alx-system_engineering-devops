exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
}

