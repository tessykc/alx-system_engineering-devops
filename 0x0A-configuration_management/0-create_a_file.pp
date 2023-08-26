# creates a file in the /tmp directory
file { '/tmp/school':
  ensure  => 'file',
  permission    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
