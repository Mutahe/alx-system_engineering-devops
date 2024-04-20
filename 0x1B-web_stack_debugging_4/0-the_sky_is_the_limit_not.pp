# Increase the amount of traffic an Nginx server can handle.

# Increae the ULIMIT
exec { 'fix--for-nginx':
  # modify value of ULIMIT
  command => '/bib/sed -i "s/15/4096/" /etc/default/nginx',
  # path specification
  path => 'usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d nginx restart',
  path => '/etc/init.d/',
}
