# This manifest kill a process called Killmenow

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
}
