import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", ['python-minimal', 'sudo'])
def test_install_dependencies(host, name):
    package = host.package(name)
    assert package.is_installed


def test_unprivileged_user_groups(host):
    unprivileged_user = host.user('vagrant')

    assert 'sudo' in unprivileged_user.groups


def test_authorized_keys_file(host):
    authorized_keys_file = host.file('/home/vagrant/.ssh/authorized_keys')

    assert authorized_keys_file.exists
    assert authorized_keys_file.user == 'vagrant'
    assert authorized_keys_file.group == 'vagrant'
    assert authorized_keys_file.contains('^ssh-rsa *')


def test_dropbear_defaults_file(host):
    dropbear_defaults_file = host.file('/etc/default/dropbear')

    assert dropbear_defaults_file.exists
    assert dropbear_defaults_file.user == 'root'
    assert dropbear_defaults_file.group == 'root'
    assert dropbear_defaults_file.contains('^NO_START=0*')
