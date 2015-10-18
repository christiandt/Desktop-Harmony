from harmony import auth
from harmony import client

username = "mail@mail.com"
password = "PW"

ip = "10.0.0.0"
port = "5222"

token = auth.login(username, password)
session_token = auth.swap_auth_token(ip, port, token)
harmony_client = client.create_and_connect_client(ip, port, token)

configuration = harmony_client.get_config()

counter = 0
for activity in configuration['activity']:
	print "%i: %s" % (counter, activity['label'])
	counter += 1

selection = int(input("Activity: "))
selected_id = int(configuration['activity'][selection]['id'])

harmony_client.start_activity(selected_id)

harmony_client.disconnect(send_close=True)
