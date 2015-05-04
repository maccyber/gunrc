import socket
import sys
import logging
import urllib.request
import xml.etree.ElementTree as ET

def readXmlResponse(xmlstring, needle):
	try:
		tree = ET.ElementTree(ET.fromstring(xmlstring))
		root = tree.getroot()
		response = root.find(needle).text
	except Exception as msg:
		response = 'Could not get response from device: ' + str(msg)
	return response

def sendToDevice(server, port, sendcode, method):
	logger = logging.getLogger('gunrc')
  
	if method == "http":
		try:
			returnmessage = 'Could not send command to device'
			logger.debug("http")
			url = 'http://' + server + '/web/' + sendcode
			logger.info('Sending data: %s %s', sendcode, url)
			data = urllib.request.urlopen(url)
			content = data.read().decode('utf-8')
			if content:
				response = readXmlResponse(content, 'e2resulttext')
				returnmessage = response
				logger.debug(response)
				logger.debug(content)
			
		except Exception as msg:
			returnmessage = 'Could not send command to device: ' + str(msg)
		return returnmessage
	else:
		logger.debug("telnet")
		returnmessage = 'Could not send command to device'

		# Send singal to device
		try:
			# Create socket
			clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# Set timout
			clientsocket.settimeout(2)

			# Connect to device
			logger.debug('Connecting to device: %s:%s', server, port)
			clientsocket.connect((server, int(port)))
			data = sendcode+'\r\n'
			logger.info('Sending data: %s', data)
			clientsocket.send(data.encode())
			reply, server_address_info = clientsocket.recvfrom(1024)
			errorCode = b'E04\r\n'
			#humanReadReply = reply.decode('utf-8')
			if reply == errorCode:
				returnmessage = 'Device did not understand command' + sendcode
				logger.error('Device did not understand command %s' %sendcode)
			else:
				returnmessage = 'Data sent successfully'
				logger.info('Data sent successfully')
			clientsocket.close()

		except Exception as msg:
			returnmessage = 'Could not send command to device: ' + str(msg)
			logger.error(msg)

		return returnmessage

