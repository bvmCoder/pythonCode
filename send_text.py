from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
# What python keyword Python means?

account_sid = "ACbb20b4855d697de59752b9122f6e5aba"
auth_token = "afb5815a604e708e79b684959c9c27a2"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create (
	body = "Hey Twilio?! What is going on? <3",
	to = "+15169437777", 	# Replace with your phone number
	from_ = "+15165950715" 	# Replace with your Twilio number
)		     
print message.sid