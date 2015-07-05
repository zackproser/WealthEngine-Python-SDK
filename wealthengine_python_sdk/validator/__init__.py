import re 

class Validator: 

	def isValidEnvironment(self, env):
		"""Return <bool> representing whether or not passed in env param is valid

			:param env - <string> Name of the requested WealthEngine API environment

		"""
		if (type(env) is not str or not env): 
			raise ValueError('You must pass a valid api environment as a string (test / prod).')
		env = env.strip()
		environs = ["prod", "production", "test", "sandbox"]
		if any(env in e for e in environs):
			return True
		else:
			return False

	def isValidApiKey(self, apiKey):
		"""Return <bool> representing whether or not passed in apiKey param is valid

			:param apiKey - <string> The user's APIKey from dev.wealthengine.com

		"""
		if (type(apiKey) is not str or not apiKey):
			raise ValueError('You must pass a valid apiKey as a string - see dev.wealthengine.com for details.') 
		return True	

	def isValidEmailRequest(self, dict):
		"""Return <bool> representing whether or not email lookup request params are valid

			:param dict - <dictionary> Dictionary containing the email endpoint POST parameters

		"""
		if (not dict["email"] or type(dict["email"]) is not str):
			raise ValueError("You must pass a valid email as a string to getProfileByEmail method")
		if (dict["first_name"]):
			if (type(dict["first_name"]) is not str):
				raise ValueError("You must pass a valid name as a string for the first_name parameter")  
		if (dict["last_name"]):
			if (type(dict["last_name"]) is not str): 
				raise ValueError("You must pass a valid name as a string for the last_name parameter")
		return True 

	def isValidAddressRequest(self, dict): 
		"""Return <bool> representing whether or not address lookup request params are valid

			:param dict - <dictionary> Dictionary containing the address endpoint POST parameters

		"""
		if (not dict["zip"] or type(dict["zip"]) is not int or len(str(dict["zip"])) != 5): 
			raise ValueError('You must pass a valid 5 digit zipcode as an integer to the getProfileByAddress method')
		for field, value in dict.iteritems():
			if (field == 'zip'): 
				pass
			elif (not value or type(value) is not str): 
				raise ValueError('getProfileByAddress requires valid strings for first_name, last_name, address_line1, city, and state')
		return True

	def isValidPhoneRequest(self, dict):
		"""Return <bool> representing whether or not phone lookup request params are valid

			:param dict - <dictionary> Dictionary containing the phone endpoint POST parameters
		""" 
		if (not dict["phone"] or type(dict["phone"]) is not str or not dict["phone"].isdigit()): 
			raise ValueError('You must pass a valid phone number, as a string containg digits only, to the getProfileByPhone method')
		if (dict["first_name"]):
			if (type(dict["first_name"]) is not str):
				raise ValueError('You must pass a valid first_name parameter as a string to the getProfileByPhone method')
		if (dict["last_name"]): 
			if (type(dict["last_name"]) is not str): 
				raise ValueError('You must pass a valid last_name parameter as a string to the getProfileByPhone method')
		return True

	def isAValidSessionRequest(self, dict): 
		"""Return <bool> representing whether or not session create request params are valid

			:param dict - <dictionary> Dictionary containing the session create endpoint POST params

		"""
		if (dict["duration"]):
			if (type(dict["duration"]) is not int): 
				raise ValueError('Session duration must be a valid integer representing the requested session duration in milliseconds') 
		return True