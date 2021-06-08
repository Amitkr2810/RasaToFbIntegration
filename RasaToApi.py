import requests

sender = input("type your name\n")

bot_message =" "

while bot_message !="Bye":
    message = input("Type your message\n")
    print("Sending now")
    r=requests.post('http://localhost:5005/webhooks/rest/webhook' , json={"sender": sender, "message":message})
    print("bot says,", end='')

    # print(r.json())
    for i in r.json():
        bot_message=i['text']
        print(bot_message)
