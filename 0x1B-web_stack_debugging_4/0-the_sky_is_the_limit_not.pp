# Puppet Manifest to Optimize Nginx Configuration

# Resource to fix Nginx configuration
exec { 'fix--for-nginx':
  command     => '/usr/sbin/nginx -s reload',  # Reload Nginx server
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,                          # Only execute when notified
  subscribe   => Package['nginx'],              # Subscribe to Nginx package changes
  notify      => Service['nginx'],              # Notify Nginx service to restart
}
