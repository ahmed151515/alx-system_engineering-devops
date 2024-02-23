exec { 'killmenow':
  path     => '/bin:/usr/bin',
    command => 'pkill -f killmenow',
}
