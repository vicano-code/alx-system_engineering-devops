# Fix the OS configuration so that it is possible to login with the holberton user and open a file without any error message

$user = 'holberton'

# Ensure the soft nofile limit is set
exec { 'set soft nofile limit':
  command => "sed -i '/^${user} soft nofile/ c\\${user} soft nofile 4096' \\
              /etc/security/limits.conf || echo '${user} soft nofile 4096' >> /etc/security/limits.conf",
  unless  => "grep -q '^${user} soft nofile 4096\$' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Ensure the hard nofile limit is set
exec { 'set hard nofile limit':
  command => "sed -i '/^${user} hard nofile/ c\\${user} hard nofile 8192' \\
              /etc/security/limits.conf || echo '${user} hard nofile 8192' >> /etc/security/limits.conf",
  unless  => "grep -q '^${user} hard nofile 8192\$' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
