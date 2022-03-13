# Create a manifest that kills a process 'killmenow'

exec {'/usr/bin/pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
