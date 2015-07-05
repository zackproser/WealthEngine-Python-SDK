from wealthengine_python_sdk import WealthEngineClient 

#Instantiate the WealtheEngine SDK with API Key and Environment
WeAPI = WealthEngineClient('ddb26e11-9348-4ead-9e2a-5a3b80a01b52', 'prod')

#Look up a WealthEngine Profile by email address
post_fields = {
	"email": "zackproser@gmail.com", 
	"first_name": "zack", 
	"last_name": "proser"
}

print WeAPI.getProfileByEmail(post_fields)

#Look up a WealthEngine profile by address
post_fields = {
	"first_name": "Hamburt", 
	"last_name": "Porkington", 
	"address_line1": "756 Jambon Dr", 
	"city": "Baton Rouge", 
	"state": "LA",
	"zip": 70801
}

print WeAPI.getProfileByAddress(post_fields)


#Look up a WealthEngine profile by phone number
post_fields = {
	"first_name": "Hamburt", 
	"last_name": "Porkington", 
	"phone": "1231231234"
}

print WeAPI.getProfileByPhone(post_fields)

#Create a session - passing desired duration in milliseconds
post_fields = {
	"duration": 7200
}

print WeAPI.createSession(post_fields)
