from twilio.rest import Client


account_sid = "ACf2cd378a6e6be17d7150cd3b0ac068b1"
account_key = "b18c72a5beb04a17aff49b4e14f06b7b"
client = Client(account_sid, account_key)
message = client.messages.create(
    to="<phone number with country code>",
    from_="<twilio Phone number>",
    body="Hi, This is Rupesh")
print(message.sid)
