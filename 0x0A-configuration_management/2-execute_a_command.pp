# solve task
exec { 'killmenow':
  path      => '/bin:/usr/bin:usr/sbin',
    command => 'pkill  killmenow',
}
