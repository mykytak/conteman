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

        vagrantfile = state.path + '/Vagrantfile'

        cls._sed('"base"', '"ubuntu\/trusty64"', vagrantfile)

        network ='''\
  config.vm.network "public_network", type: "dhcp"\\n\
  config.vm.hostname = "{}.dev"\\n\
  config.landrush.enabled = true\\n\
  config.landrush.tld = ".dev"\\n\
  config.landrush.guest_redirect_dns = false'''.format(state.projname)


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
