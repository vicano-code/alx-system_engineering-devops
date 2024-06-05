# Puppet file to automate process to fix Apache2 error code 500

file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Create a simple index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my website. This is a simple HTML file served by Apache.</p>
</body>
</html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => File['/var/www/html'],
}
