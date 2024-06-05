# Puppet file to automate process to fix Apache2 error code 500

file { '/var/www/html/index.html':
  ensure  => file,
  require => File['/var/www/html'],
}

# apply fix for wrong file name extension
exec { 'rename-wrong-file':
  command => '/bin/mv /var/www/html/wp-includes/class-wp-locale.phpp /var/www/html/wp-includes/class-wp-locale.php',
  onlyif  => 'test -e /var/www/html/wp-includes/class-wp-locale.phpp',
  require => File['/var/www/html/wp-includes/class-wp-locale.php'],
}
