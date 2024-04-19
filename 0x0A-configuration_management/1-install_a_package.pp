# This manifest will install Flusk using pip3
# Ensure the puppetlabs/stdlib module is installed
class { 'stdlib': }

# Ensure the puppetlabs/python module is installed
class { 'python': }

# Install Flask version 2.1.0 using pip3
python::pip { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
