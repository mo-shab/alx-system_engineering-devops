# This manifest will Create a file in /tmp with permission 0744, owner www-data, group www-data content "i love Puppet"
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
}
