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


        cmd = '''sed '/^a test$/{
       $!{ N        # append the next line when not on the last line
         s/^{}$/{}/
                    # now test for a successful substitution, otherwise
                    #+  unpaired "a test" lines would be mis-handled
         t sub-yes  # branch_on_substitute (goto label :sub-yes)
         :sub-not   # a label (not essential; here to self document)
                    # if no substituion, print only the first line
         P          # pattern_first_line_print
         D          # pattern_ltrunc(line+nl)_top/cycle
         :sub-yes   # a label (the goto target of the 't' branch)
                    # fall through to final auto-pattern_print (2 lines)
       }    
     }' {}  '''.format('\'# config.vm.network "public_network"\'', network, vagrantfile)

        call(cmd, shell=True)
