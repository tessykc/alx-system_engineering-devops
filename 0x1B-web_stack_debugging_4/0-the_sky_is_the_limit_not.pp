# Define class to manage Nginx configuration
class nginx_module::nginx_config {

  # Ensure Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Define Nginx configuration file
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('nginx_module/nginx.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}
