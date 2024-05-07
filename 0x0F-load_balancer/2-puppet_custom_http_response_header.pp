# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec {'update system':
	command  => 'sudo apt-get update',
	provider => shell,
}

package {'nginx':
	ensure  => installed,
	require => Exec['update'],
}

file_line {'headercustom':
	ensure  => present,
	path    => '/etc/nginx/sites-available/default',
	after   => ':80 default_server;',
	line    => "add_header X-Served-By ${hostname};",
	require => Package['nginx'],
}

exec {'redirect_me':
	command => 'sed -i "48i "\\\tlocation /redirect_me {\n\t\treturn 301 https://google.com;\n\t}\n" /etc/nginx/sites-available/default,
	provider => 'shell',
}

service {'nginx':
	ensure => running,
	require => File_line['headercustom'],
}
