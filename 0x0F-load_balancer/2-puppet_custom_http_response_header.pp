# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec {'update system':
	command => '/usr/bin/apt-get update'
}

package {'nginx':
	ensure => 'installed'
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "48i "\\\tlocation /redirect_me {\n\t\treturn 301 https://google.com;\n\t}\n" /etc/nginx/sites-available/default,
	provider => 'shell'
}

nginx::resource::location { 'add_custom_header':
	location => '/',
	header   => 'X-Served-By $hostname',
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
