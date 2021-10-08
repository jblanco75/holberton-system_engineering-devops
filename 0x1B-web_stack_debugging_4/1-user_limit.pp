# This script changes the os configuration, to login with the holberton user and open a file witouh any error message.
exec {'Updating nofile hard':
  command => "sudo sed -i 's,holberton hard nofile.*,holberton hard nofile 5000,' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}
exec {'Updating nofile soft':
  command => "sudo sed -i 's,holberton soft nofile.*,holberton soft nofile 5000,' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}