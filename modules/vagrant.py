import logging, sys, os
from subprocess import call, getoutput

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver

def register():
  CommandObserver.register('vagrant:create' , Vagrant.create)
  CommandObserver.register('vagrant:open'   , Vagrant.open)

class Vagrant():
    @classmethod
    def create(cls, state):
        cmd = 'cd {}; vagrant init'.format(state.path)

        call(cmd, shell=True)
        # "ubuntu/trusty64"

        vagrantfile = state.path + '/Vagrantfile'

        call('sed -i s/{}/{}/ {}'.format('"base"', '"ubuntu\/trusty64"', vagrantfile))

        network ='''\
  config.vm.network "public_network", type: "dhcp"\\n\
  config.vm.hostname = "{}.dev"\\n\
  config.landrush.enabled = true\\n\
  config.landrush.tld = ".dev"\\n\
  config.landrush.guest_redirect_dns = false'''.format(state.name)


        # doesn't work again. wtf?
        cmd = '''sed -i '/^{}/{{
       $!{{ N        # append the next line when not on the last line
         s/^{}/{}/
                    # now test for a successful substitution, otherwise
                    #+  unpaired "a test" lines would be mis-handled
         t sub-yes  # branch_on_substitute (goto label :sub-yes)
         :sub-not   # a label (not essential; here to self document)
                    # if no substituion, print only the first line
         P          # pattern_first_line_print
         D          # pattern_ltrunc(line+nl)_top/cycle
         :sub-yes   # a label (the goto target of the 't' branch)
                    # fall through to final auto-pattern_print (2 lines)
       }}    
     }}' {}
         '''


        cmd = cmd.format('  # config.vm.network "public_network"', '  # config.vm.network "public_network"', network, vagrantfile)

        call(cmd, shell=True)

    @staticmethod
    def open(state):
        logging.debug('Vagrant:open, state %s', state)

        output = getoutput("cd {}; vagrant up".format(state.path)) #, shell=True

        logging.debug('Vagrant output: %s', output)
