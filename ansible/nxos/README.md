# NXOS Ansible playbooks

This directory is for testing Ansible playbooks against NXOS.
Typically the target is the Cisco NX-OS Sandbox at:

          ansible_host: 131.226.217.151
          ansible_ssh_user: admin
          ansible_ssh_password: "Admin_1234!"

# Tips

Installing pylibssh was a bit fiddly, libssh can be installed with homebrew:

```
brew install libssh
```

But then you need to make pip use the /opt/homebrew include and lib dirs:

```
export CPPFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib"; pip install ansible-pylibssh
...
Successfully installed ansible-pylibssh-1.2.2
```

This workaround is from https://stackoverflow.com/questions/19071708/pip-install-customized-include-path
