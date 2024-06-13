# Fix Nginx accept4() failed (24: Too many open files) requests

exec {'modify user limit open file size':
  command => 'sed -i "s/15/5000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
