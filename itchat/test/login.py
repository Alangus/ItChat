import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg.text == "贾子昂":
        return "是全世界最帅的人"
    else:
        return msg.text


itchat.auto_login(enableCmdQR=2)
itchat.run()

