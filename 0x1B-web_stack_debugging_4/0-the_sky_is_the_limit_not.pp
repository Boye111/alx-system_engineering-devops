# testing how well our web server setup featuring Nginx is doing under pressure

exec { 'fix--for-nginx':
	command => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'"
}

exec { 'restart nginx':
	command => '/usr/sbin/service nginx restart',
	require => Exec['fix--for-nginx']
}