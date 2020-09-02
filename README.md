# Server Pre-Ansible Playbook

Generic ansible playbook for servers that will setup the basic configurations
and programs so it's a stable machine for deploying the services and
configurations afterwards.

## Description

This playbook will cover:

* Install `python` and `sudo` on the target host(s). So ansible can run
   properly.
* Setup a `busybox` and `dropbear` SSH server in the initramfs with a static IP
   so you can remotely login to the server and unlock the LUKS encrypted disks.

## Compatibility

This role should work in any distro from the **Debian** family. It is tested
on debian buster.

## Requirements

`python` and `sudo`.

## Dependencies

Included as submodules in *roles/*. To fetch them automatically when cloning,
use:

```bash
git clone --recurse-submodules -j10 [repo]
```

* [dropbear_luks](https://github.com/anarres-org/dropbear_luks)
* [ansible-role-interfaces](https://github.com/michaelrigart/ansible-role-interfaces)
* [ddclient](https://github.com/anarres-org/ddclient)

## Playbook Variables

### ansible-role-interfaces

You must include directly the variables for this role if used.

For example:

```yaml
interfaces_ether_interfaces:
 - device: eth1
   bootproto: static
   address: 192.168.1.150
   netmask: 255.255.255.0
   gateway: 192.168.1.1
   dnsnameservers: 192.0.2.1 192.0.2.2
```

### dropbear_luks

You must fill the variables with the **dropbear.** prefix. They are the same
names from the role.

### ddclient

You must include directly the variables for this role if used.

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/)
. You also need to have a valid SSH public key in *~/.ssh/id_rsa.pub*. If you
don't have one, you can create it with: `ssh-keygen -C test -f ~/.ssh/id_rsa`.

```bash
molecule test
```

## License

GPLv3

## Author Information

m0wer: m0wer (at) autistici (dot) org
