import logging
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from config import Config
from xmlmap import xmlmap
from sendsocket import sendToDevice

logger = logging.getLogger('gunrc')

# Init config
cfg = Config(0)

class window1():

	def __init__(self):
		# GTK-Builder stuff
		self.builder = Gtk.Builder()
		self.builder.add_from_file('ui/ui.glade')
		self.builder.connect_signals(self)

		# Main Window
		self.window = self.builder.get_object('mainwindow')
		self.comboProfile = self.builder.get_object('comboProfile')

		# Populate profile combo
		self.repopulateProfiles(self.comboProfile)
		self.comboProfile.set_active(0)

		# Settings Window
		self.settingswindow = self.builder.get_object('settingswindow')

		# Dialog for config
		self.errordialog = self.builder.get_object('messagedialog')

		# Entries and such
		self.entryProfile = self.builder.get_object('entryProfile')
		self.entryServer = self.builder.get_object('entryServer')
		self.entryPort = self.builder.get_object('entryPort')
		self.entryXml = self.builder.get_object('entryXml')
		self.radioTelnet = self.builder.get_object('radioTelnet')
		self.radioHttp = self.builder.get_object('radioHttp')
		self.comboProfileConfig = self.builder.get_object('comboProfileConfig')
		self.statusbar = self.builder.get_object('statusbar')

		# Show Main Window on init
		self.window.show()

	# Repopulate profiles
	def repopulateProfiles(self, widget):
		# Refresh from config
		cfg = Config(0)
		sections = cfg.getSections()

		# Clear profiles
		widget.get_model().clear()

		# Append new
		for profile in sections:
 			widget.append(profile, profile)

	# Send code to device
	def sendCodeToDevice(self, code):
		# Get from config
		server = cfg.getValue('active', 'server')
		port = cfg.getValue('active', 'port')
		xml = cfg.getValue('active', 'xml')
		method = cfg.getValue('active', 'method')

		# Update statusbar
		self.statusUpdate('Sending: <%s> to device' %code)

		# Convert sendcode from XML map
		sendcode = xmlmap(xml, code)

		# If sendcode was found and converted OK
		if sendcode:
			# Send sendcode to device
			resp = sendToDevice(server, port, sendcode, method)

			# and update statusbar with device response
			self.statusUpdate(resp)
		else:
			# If sendcode was not found, give error messag
			self.statusUpdate('No keycode found in XML for command: %s' %sendcode)

	# Get active index from combobox
	def get_active_index(self, combobox):
		self.index = combobox.get_active()
		return self.index

	# Get active text from combobox
	def get_active_text(self, combobox):
		model = combobox.get_model()
		active = combobox.get_active()
		if active < 0:
			return False
		return model[active][0]

	# Destroys window
	def destroy(self, widget):
		logger.debug('User killed window')
		Gtk.main_quit()

	# Hides window
	def hide(self, window, data):
		logger.debug('User hided window')
		window.hide()
		return True

	# Refreshes status
	def statusRefresh(self, widget, msgid):
		self.statusbar.remove(0,msgid)

	# Update statusbar with timeout
	def statusUpdate(self, text):
		#self.statusbar = self.builder.get_object('statusbar')
		msgid = self.statusbar.push(0, text)
		timeoutid = GObject.timeout_add(7000, self.statusRefresh, self, msgid)  

	# When window gets killed
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)

	# Button and combo handlers for mainwindow
	def comboProfileChanged(self, widget, data=None):
		activeText = self.get_active_text(self.comboProfile)
		if not activeText:
			return
		cfg.set('general', 'active', activeText)
		cfg.writeConfig()
		logger.debug('Active profile is %s', activeText)

	def comboInputChanged(self, widget, data=None):
		self.index = widget.get_active()
		self.model = widget.get_model()
		self.item = self.model[self.index][1]
		self.sendCodeToDevice(self.item)

	def toggleShutdownToggled(self, button):
		self.sendCodeToDevice('poweron')

	def toggleZone2(self, button):
		self.sendCodeToDevice('zone2poweron')

	def btnMuteClicked(self, button):
		self.sendCodeToDevice('muteon')

	def btnZeroClicked(self, button):
		self.sendCodeToDevice('zero')

	def btnOneClicked(self, button):
		self.sendCodeToDevice('one')

	def btnTwoClicked(self, button):
		self.sendCodeToDevice('two')

	def btnThreeClicked(self, button):
		self.sendCodeToDevice('three')

	def btnFourClicked(self, button):
		self.sendCodeToDevice('four')

	def btnFiveClicked(self, button):
		self.sendCodeToDevice('five')

	def btnSixClicked(self, button):
		self.sendCodeToDevice('six')

	def btnSevenClicked(self, button):
		self.sendCodeToDevice('seven')

	def btnEightClicked(self, button):
		self.sendCodeToDevice('eight')

	def btnNineClicked(self, button):
		self.sendCodeToDevice('nine')

	def btnBackClicked(self, button):
		self.sendCodeToDevice('return')

	def btnUpClicked(self, button):
		self.sendCodeToDevice('up')

	def btnHomeClicked(self, button):
		self.sendCodeToDevice('return')

	def btnLeftClicked(self, button):
		self.sendCodeToDevice('left')

	def btnSelectClicked(self, button):
		self.sendCodeToDevice('enter')

	def btnRightClicked(self, button):
		self.sendCodeToDevice('right')

	def btnDownClicked(self, button):
		self.sendCodeToDevice('down')

	def btnChanUpClicked(self, button):
		self.sendCodeToDevice('channelup')

	def btnChanDownClicked(self, button):
		self.sendCodeToDevice('channeldown')

	def btnPlayClicked(self, button):
		self.sendCodeToDevice('play')

	def btnPauseClicked(self, button):
		self.sendCodeToDevice('pause')

	def btnStopClicked(self, button):
		self.sendCodeToDevice('stop')

	def btnVolUpClicked(self, button):
		self.sendCodeToDevice('volumeplus')

	def btnVolDownClicked(self, button):
		self.sendCodeToDevice('volumeminus')
	
	def btnOptOneClicked(self, button):
		self.sendCodeToDevice('optone')
	
	def btnOptTwoClicked(self, button):
		self.sendCodeToDevice('opttwo')
	def btnGreenClicked(self, button):
		self.sendCodeToDevice('green')
	def btnRedClicked(self, button):
		self.sendCodeToDevice('red')
	def btnYellowClicked(self, button):
		self.sendCodeToDevice('yellow')
	def btnBlueClicked(self, button):
		self.sendCodeToDevice('blue')

	def btnSettingsClicked(self, button):
		logger.debug('Opened settings window')
		self.repopulateProfiles(self.comboProfileConfig)
		self.comboProfileConfig.insert_text(0, '<New profile>')
		self.comboProfileConfig.set_active(0)

		self.settingswindow.show()

	# Handlers for settings window
	def comboProfileConfigChanged(self, widget, data=None):
		activeText = self.get_active_text(self.comboProfileConfig)

		# Don't bother with anything when building comboProfile
		if not activeText:
			return
		activeIndex = self.get_active_index(self.comboProfileConfig)
		entryProfile = ''
		entryProfileEdit = True

		server = ''
		port = ''
		xml = ''
		method = ''

		# If not default <new profile>
		if activeIndex > 0:
			entryProfileEdit = False
			entryProfile = activeText

			server = cfg.getValue(entryProfile, 'server')
			port = cfg.getValue(entryProfile, 'port')
			xml = cfg.getValue(entryProfile, 'xml')
			method = cfg.getValue(entryProfile, 'method')


		self.entryProfile.set_text(entryProfile)
		self.entryServer.set_text(server)
		self.entryPort.set_text(port)
		self.entryXml.set_text(xml)
		self.entryProfile.set_sensitive(entryProfileEdit)
		if method == "http":
			self.radioHttp.set_active(True)
		else:
			self.radioTelnet.set_active(True)

		logger.debug('Config active config profile is %s', activeText)

	def btnSaveClicked(self, button):
		profile =  self.entryProfile.get_text()
		server = self.entryServer.get_text()
		port =  self.entryPort.get_text()
		xml =  self.entryXml.get_text()
		if self.radioHttp.get_active():
			method = "http"
		else:
			method = "telnet"

		if not (profile and server and port and xml):
			logger.info('Required fields not filled out')
			self.errordialog.run()
		else:
			# if section don't exist - create it
			if not cfg.hasSection(profile):
				cfg.createSection(profile)

			cfg.set(profile, 'server', server)
			cfg.set(profile, 'port', port)
			cfg.set(profile, 'xml', xml)
			cfg.set(profile, 'method', method)
			cfg.writeConfig()

			logger.debug('Button Save clicked')
			logger.debug('Profile: %s', profile)
			logger.debug('Server: %s', server)
			logger.debug('Port: %s', port)
			logger.debug('Method: %s', method)
			logger.debug('XML-file: %s', xml)
			logger.info('Saved config')

			self.repopulateProfiles(self.comboProfile)		
			self.settingswindow.hide()

	def btnDialogClicked(self, button, response):
		self.errordialog.hide()

	def btnCancelClicked(self, button):
		self.settingswindow.hide()
		logger.debug('Pressed cancel in settingswindow')

	def btnDeleteClicked(self, button):
		activeIndex = self.get_active_index(self.comboProfileConfig)
		activeText = self.get_active_text(self.comboProfileConfig)
		
		if activeIndex > 0:
			cfg.deleteSection(activeText)
			logger.info('Deleted %s', activeText)
			self.comboProfileConfig.set_active(0)
			self.repopulateProfiles(self.comboProfile)
			self.settingswindow.hide()
		else:
			print('give error')
		
def builder():	

	# Show window
	main = window1()
	Gtk.main()
screen = Gdk.Screen.get_default()

css_provider = Gtk.CssProvider()
css_provider.load_from_path('ui/style.css')

context = Gtk.StyleContext()
context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
