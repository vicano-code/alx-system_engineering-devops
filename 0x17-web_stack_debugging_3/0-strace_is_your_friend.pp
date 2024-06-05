# Puppet file to automate process to fix Apache2 error code 500
# Error found using strace says no index.html file.
# Using puppet to create file with content

# Ensure the /var/www/html directory exists with correct ownership and permissions
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

# Ensure the Apache service is running and enabled
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.html'],
}
