import xml.etree.ElementTree as et
import logging

def xmlmap(xml, command):
	logger = logging.getLogger('gunrc')

	try:
		# XML read
		tree = et.parse(xml)

		# Get root
		root = tree.getroot()

		# Find device name
		logger.debug('Device: %s', root.get('device'))

		# Find remotecode
		sendcode = root.find(command).text
		if not sendcode:
			raise Exception('No keycode found in XML for command \"'+command+'\"')
		logger.info('Command to send: %s', sendcode)
	except Exception as msg:
		logger.error(msg)
		sendcode = False
	return sendcode

def listAll(xml):
	# XML read
	tree = et.parse(xml)

	# Get root
	root = tree.getroot()

	for child in root:
		print (child.tag)
