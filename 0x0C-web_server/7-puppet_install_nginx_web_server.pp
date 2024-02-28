# solve task

package { 'nginx':
  ensure   => installed,
  provider => 'apt-get'
}


service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    listen [::]:80;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files ${uri} ${uri}/ =404;
    }

    location /redirect_me {
        return 301 https://www.example.com/;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}


file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

