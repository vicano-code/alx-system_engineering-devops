# Puppet file to fix typo in wordpress config file causing apache2 error code 500

exec { 'fix typo in wp-settings.ph file':
  command => "sed i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
