# Puppet manifest to debug and optimize the Nginx server configuration

# Define the Nginx service
service { 'nginx':
  ensure => running, # Ensure the service is running
}

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file, # Ensure it's a file
  content => template('nginx/default.erb'), # Use a template for configuration
  notify  => Service['nginx'], # Notify the service of changes
}

# Define a custom Nginx configuration template
file { '/etc/nginx/default.erb':
  ensure  => file,
  content => '# Optimized Nginx configuration goes here',
}

