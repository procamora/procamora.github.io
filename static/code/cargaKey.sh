#!/usr/bin/expect -f

set USER [exec whoami]

spawn ssh-add /home/$USER/.ssh/OpenSSH
expect "Enter passphrase for /home/$USER/.ssh/OpenSSH:"
send "PASSWORD$\n";
interact
