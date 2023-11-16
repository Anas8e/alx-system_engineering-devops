# Puppet Manifest to Optimize Nginx Configuration

exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',  # Command to reload Nginx service
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,                              # Execute only on trigger
  unless      => '/usr/sbin/service nginx status | grep "not running"', # Check if Nginx is not running
  logoutput   => true,                              # Log the output of the command
  notify      => Service['nginx'],                  # Notify the Nginx service
}
