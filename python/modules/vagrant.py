from subprocess import call

class Vagrant():
    @staticmethod
    def _sed(what, to, file):
        call('sed -i s/{}/{}/ {}'.format(what, to, file), shell=True)

    @classmethod
    def create(cls, state):
        cmd = 'cd {}; vagrant init'.format(state.path)

        call(cmd, shell=True)
        # "ubuntu/trusty64"

        vagrantfile = state.path + '/Vagrant'

        cls._sed('"base"', '"ubuntu\/trusty64"', vagrantfile)
        
        network ='''  config.vm.network "public_network", type: "dhcp"\n  config.vm.hostname = "{}.dev"
  config.landrush.enabled = true
  config.landrush.tld = ".dev"
  config.landrush.guest_redirect_dns = false'''.format(state.projname)
        cls._sed('\'# config.vm.network "public_network"\'', network, vagrantfile)
