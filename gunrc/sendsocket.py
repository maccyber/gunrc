import socket
import sys
import logging

def sendToDevice(server, port, sendcode):
	logger = logging.getLogger('gunrc')
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

