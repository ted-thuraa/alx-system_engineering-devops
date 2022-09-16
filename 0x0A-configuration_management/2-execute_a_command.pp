# puppet stuff

exec { 'kill process':
	command => "pkill 'killmenow'",
	path => '/usr/bin/'
}
