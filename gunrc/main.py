#!/usr/bin/python

import argparse
import sys
import logging
from config import Config
from xmlmap import xmlmap, listAll
from ui import builder
from sendsocket import sendToDevice
import cli

def main(argv):
	# Turn on logging
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger('gunrc')

	args = cli.Args()

	print(args.appdesc)
	
	args.parser(argv)

	if args.get.debug:
		logger.setLevel(logging.DEBUG)
		logger.debug('Debug started')

	if args.get.run_cmd:
		# Run in console
		profile = args.get.run_cmd[0]
		logger.debug('Profile parm: %s', profile)

		command = args.get.run_cmd[1]
		logger.debug('Command parm: %s', command)

		cfg = Config(profile)
		
		server = cfg.getValue(profile, 'server')
		logger.debug('Server: %s', server)

		port = cfg.getValue(profile, 'port')
		logger.debug('Port: %s', port)

		xml = cfg.getValue(profile, 'xml')
		logger.debug('XML-file: %s', xml)
		
		sendcode = xmlmap(xml, command)

		if sendcode:
			sendToDevice(server, port, sendcode)
	elif args.get.list:
		cfg = Config(0)
		# List
		if args.get.list == 'profiles':
			print('Available profiles:\n')
			for i in cfg.sections:
				print(i)
			sys.exit()
		else:
			print('Available commands:\n')
			listAll('/usr/share/gunrc/template.xml')
			sys.exit()

	else:
		# Run GUI
		builder()

if __name__ == '__main__':
	main(sys.argv[1:])

