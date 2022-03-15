# configure ssh client configuration file

$username = $facts['identity']['user']
file {"/home/${username}/.ssh/config":
  ensure => file,
  content => "Host 3.94.99.147\n \tIdentityFile ~/.ssh/school\n \tPasswordAuthentication no\n"
}
