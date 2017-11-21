import itchat
import time


@itchat.msg_register('Text',isGroupChat=True)
def group_text_reply(msg):
    print(msg)
    if '联系人 韩荣' in msg['Content']:
        print('抢单')
        itchat.send_msg(u"报名", msg['ToUserName'])
        itchat.send_msg(u"[%s]收到@%s的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                            msg['User']['NickName'],
                            msg['Text']), 'filehelper')

if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()