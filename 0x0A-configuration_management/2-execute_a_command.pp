# solve task
exec { 'killmenow':
  path     => '/bin:/usr/bin',
    command => 'pkill  killmenow',
}
