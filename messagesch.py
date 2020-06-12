from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
def newmessage(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Maybe now you can! <3',      
                              to='whatsapp:+918376934043' 
                          ) 
 
    print(message.sid)