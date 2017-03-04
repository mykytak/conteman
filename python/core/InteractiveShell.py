import imp, os


class InteractiveShell():

	configs = {}
	choices = {}

	def __set__(self, name, value):
		self.choices.name = value


	# def __init__(self):


	def build_user_config(self, obj):
    configs = {}
    configs['git'] = {}
    configs['firefox'] = {}
    configs['project_name'] = input("Your Project Name : ")
    configs['git']['username'] = input("Your Git Username: ")
    configs['git']['email'] = input("Your Git Email: ")
    configs['firefox']['profile'] = input("Firefox Profile: ")

    print('Check Once More: \n \
    Project Name: ' + configs['project_name'] \
    + '\n Git config email: ' + configs['git']['username'] \
    + '\n Git config email: ' + configs['git']['email'] \
    + '\n Firefox Profile: ' + configs['firefox']['profile'])

    confirmation = input("Confirm choice Y/n : ")

    if confirmation == 'Y':
        print('Yep')
        return configs
    else:
        print('Why?!')
        return build_user_config()
