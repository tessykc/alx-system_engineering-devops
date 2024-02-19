# Define a class for Nginx installation and configuration
class nginx_server {
  
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    content => "<html><body><h1>Hello World!</h1></body></html>",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    source  => 'puppet:///modules/nginx_server/default',
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    hasstatus => true,
    require   => Package['nginx'],
  }
}

# Configure the default Nginx server block for redirection
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;
    server_name _;

    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 http://example.com/destination_page;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
  ",
}
