import argparse

class Args:

	bold = '\033[1m'
	end = '\033[0m'
	line = '+' + '-' *47 + '+'
	name = '|' + bold + '    G' + end + 'tk ' + bold + 'U' + end + 'niversal ' + bold + 'N' + end + 'etwork ' + bold + 'R' + end + 'emote' + bold + 'C' + end + 'ontrol        |'
	logo = '''
|    ______.                                    |
|  ~(_]----' °¹°¹°                              |
|  /_(  GunRC v0.1                              |
|                                               |
'''
	appdesc = line + '\n' +  name + logo + line + '\n'


	def __init__(self):
		self.skip_gui = True
		self.start_visibility = None
		self.start_shell = False
		self.get = ''

	def parser(self, argv):
		parser = argparse.ArgumentParser(description='cli example: gunrc -c default play')

		parser.add_argument('-V', '--version', action='version', version="%(prog)s (Version 0.1)")
		parser.add_argument('-d', dest='debug', action='store_true', default=False, help='turn on for debugging')
		parser.add_argument('-l', dest='list', choices=['profiles', 'commands'], help='list available profiles or commands')
		parser.add_argument('-c', nargs=2, metavar=('PROFILE', 'COMMAND'), dest='run_cmd', help='send COMMAND to device in PROFILE')

		self.get = parser.parse_args()
