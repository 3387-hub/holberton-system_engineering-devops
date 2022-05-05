# Avoid Failed request
exec { 'failed request':
command => 'ab -c 100 -n 2000 -l localhost/'
}