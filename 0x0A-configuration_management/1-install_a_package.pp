# Using Puppet, install flask from pip3.
# Requirements:
# Install flask
# Version must be 2.1.0


# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin/',
  unless  =>  'pip3 list | grep flask',
}
