from pyrogram import Client

api_id =  19530787
api_hash = 'b9d5bec9d22501ee256ba9cee556cae7'
app = Client('sessions/aeoenzbxsx', api_id=api_id, api_hash=api_hash)
app.connect()

app.send_message('@E_7_h', 'hello')

app.disconnect()
