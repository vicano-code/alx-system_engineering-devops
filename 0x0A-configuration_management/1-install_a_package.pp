# Using Puppet, install flask from pip3.
# Requirements:
# Install flask
# Version must be 2.1.0


# First install puppetlabs-stdlib: > puppet module install puppetlabs-stdlib

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
