## @package wealthengine_python_sdk
#  A client for interacting with the WealthEngine API
#  
#  @author Zack Proser <zackproser@gmail.com> 
#  

## Validates requests before POSTing to the API 
#
#  Wraps available WealthEngine endpoints in method calls
#  

import requests
import json
from validator import Validator

class WealthEngineClient: 
	"""Abstracts interaction with the WealthEngine Public API

		Attributes: 
			PROD_ENDPOINT The url base for the WealthEngine API production environment
			TEST_ENDPOINT The url base for the WealthEngine API test environment
			apiKey The user's APIKey obtained from dev.wealthengine.com
			apiRoot The base API URL to use in API calls, as determined by user's requested 
			Validator An instance of the Validator class, which checks POST params for correctness

	"""

	#The url base for the WealthEngine API production environment
	PROD_ENDPOINT = 'https://api.wealthengine.com/v1/'

	#The url base for the WealthEngine API test environment
	TEST_ENDPOINT = 'https://api-sandbox.wealthengine.com/v1/'

	#User's API Key from dev.wealthengine.com
	apiKey = None

	#The API root depending upon the requested environment
	apiRoot = None

	#The Validation helper
	Validator = None

	def __init__(self, apiKey, env):
		self.Validator = Validator()
		self.setApiKey(apiKey)
		self.setEnvironment(env)	
		
	def setApiKey(self, apiKey):
		"""Set the user's WealthEngine API key for use in Authorization header

			:param apiKey - <string> the user's APIKey from dev.wealthengine.com

		"""
		if (self.Validator.isValidApiKey(apiKey)): 
			self.apiKey = apiKey 
			return
		else: 
			raise ValueError('Something is wrong with your API Key please verify it and try again.')	

	def setEnvironment(self, env):
		"""Set the WealthEngine API environment - used in all API calls

			:param env - <string> the user's desired WealthEngine API environment

		"""
		if (self.Validator.isValidEnvironment(env)):
			if (env == "prod" or env == "production"): 
				self.apiRoot = self.PROD_ENDPOINT
			elif (env == "test" or env == "sandbox"):
				self.apiRoot = self.TEST_ENDPOINT
			else: 
				raise ValueError('Something is wrong with your requested API Environment. Please verify it and try again.')
		return

	def getDefaultHttpHeaders(self): 
		"""Return the default Headers object common to all API calls"""
		return {
				'User-Agent': 'Wealthengine Python SDK', 
				'Content-type': 'application/json', 
				'Accept': 'application/json',
				'Cache-control': 'none',
				'Authorization': 'APIKey ' + self.apiKey
			}

	def returnAPIResponse(self, r): 
		"""Append the http status code to the response object and return to caller

			:param r - <object> a handle to the last completed request

		"""
		return { "status_code": r.status_code, "response": r.text }

	def getProfileByEmail(self, params_dict):
		"""Attempt to lookup a WealthEngine Profile by email

			:param params_dict - <dictionary> A dict containing the POST fields and their data

		"""
		#Ensure request parameters are properly formed
		if (self.Validator.isValidEmailRequest(params_dict)):
			endpoint = self.apiRoot + 'profile/find_one/by_email/basic'

			#Make the POST Request - setting headers and POST body
			r = requests.post(endpoint, headers=self.getDefaultHttpHeaders(), data=json.dumps(params_dict))

			return self.returnAPIResponse(r); 
		else: 
			return self.raiseParamsException('getProfileByEmail')
	
	def getProfileByAddress(self, params_dict):
		"""Attempt to lookup a WealthEngine Profile by address

			:param params_dict - <dictionary> A dict containing the POST fields and their data

		"""
		#Ensure request parameters are properly formed
		if (self.Validator.isValidAddressRequest(params_dict)): 
			endpoint = self.apiRoot + 'profile/find_one/by_address/basic'

			#Make the POST Request - setting headers and POST body
			r = requests.post(endpoint, headers=self.getDefaultHttpHeaders(), data=json.dumps(params_dict))

			return self.returnAPIResponse(r); 
		else:
			return self.raiseParamsException('getProfileByAddress')

	def getProfileByPhone(self, params_dict): 
		"""Attempt to lookup a WealthEngine Profile by phone

			:param params_dict - <dictionary> A dict containing the POST fields and their data

		"""
		#Ensure request parameters are properly formed
		if (self.Validator.isValidPhoneRequest(params_dict)): 
			endpoint = self.apiRoot + 'profile/find_one/by_phone/basic'

			#Make the POST Request - setting headers and POST body
			r = requests.post(endpoint, headers = self.getDefaultHttpHeaders(), data=json.dumps(params_dict))

			return self.returnAPIResponse(r); 
		else: 
			return self.raiseParamsException('getProfileByPhone');

	def createSession(self, params_dict):
		"""Attempt to create a session to authenticate future calls to the WealthEngine API

			:param params_dict - <dictionary> A dict containing the POST fields and their data

		""" 
		#Ensure request parameters are properly formed
		if (self.Validator.isAValidSessionRequest(params_dict)): 

			endpoint = self.apiRoot + 'session/create'

			r = requests.post(endpoint, headers=self.getDefaultHttpHeaders(), data=json.dumps(params_dict))
		
			return self.returnAPIResponse(r); 
		else: 
			return self.raiseParamsException('createSession'); 

	def raiseParamsException(endpoint_name): 
		"""Raise an exception due to API call parameters being mis-configured

			:param endpoint_name - <string> The name of the endpoint that is raising the exception

		"""
		raise ValueException('Your ' + endpoint_name + ' params were improperly formatted. Please check them and try again')


