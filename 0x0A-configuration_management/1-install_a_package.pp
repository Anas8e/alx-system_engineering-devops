# 1-install_a_package.pp

# Ensure the package is installed and at the required version
package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}