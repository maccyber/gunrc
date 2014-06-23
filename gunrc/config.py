import configparser
import logging
import os

logger = logging.getLogger('gunrc')

class Config:

	# Set path to configfile
	CONFIG_PATH = os.path.expanduser('~/.config/gunrc/gunrc')	

	def __init__(self, profile):
		self.profile = profile
		self.config = configparser.ConfigParser()
		self.config.read(Config.CONFIG_PATH)
		
		# Get all sections in config
		self.sections = self.config.sections()
		# Remove general
		self.sections.remove('general')

		# Set Active Profile
		self.activeProfile = self.getActiveProfile()
		
	def getActiveProfile(self):
		# If running in cmd, use parameter
		if self.profile != 0:
			return self.profile

		# Get active profile from config
		active = self.config.get('general', 'active')

		# If active profile exists in config return it
		if  self.config.has_section(active):
			return active
		else:
			# If active profile don't exist in config - return first profile
			return self.sections[0]

	# Return given value from config
	def getValue(self, profile, setting):
		if profile == "active":
			profile = self.getActiveProfile()
		# Get value from config
		if self.config.has_option(profile, setting):
			value = self.config.get(profile, setting)
			#logger.debug("Found value for %s in config", setting)
			return (value)
		else:
			#logger.warning("Could not find value for %s in config", setting)
			return

	# Return profile sections in config
	def getSections(self):
		return self.sections

	# Check if config has given section
	def hasSection(self, section):
		return self.config.has_section(section)
		
	# Create given section in config
	def createSection(self, section):
		return self.config.add_section(section)

	def deleteSection(self, profile):
		self.config.remove_section(profile)
		self.writeConfig()

	# Set given parameter to given value and save to config
	def set(self, section, parameter, value):
		self.config.set(section, parameter, value)
		#self.writeConfig()

	def writeConfig(self):
		with open(Config.CONFIG_PATH, 'w') as configfile:
			self.config.write(configfile)
