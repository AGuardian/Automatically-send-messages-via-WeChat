from __future__ import unicode_literals 
from threading import Timer
 from wxpy import *
import requests

bot = Bot() 

# linuxִ�е�½�������������
 #bot = Bot(console_qr=2,cache_path="botoo.pkl")

def get_news(): 
     """��ȡ��ɽ�ʰ�ÿ��һ�䣬Ӣ�ĺͷ���"""
     url = "http://open.iciba.com/dsapi/"
     r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note 

def send_news(): 
   try:
     contents = get_news() 

   # �����ѵ�΢�����ƣ����Ǳ�ע��Ҳ����΢���ʺš�

        my_friend = bot.friends().search(u'С��')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u"Have a good one!") 
        # ÿ86400�루1�죩������1��
        t = Timer(86400, send_news)
        t.start()
  except:

       # ���΢�����ƣ�����΢���ʺš�

        my_friend = bot.friends().search('����')[0]
        my_friend.send(u"������Ϣ����ʧ����")

 if __name__ == "__main__":
    send_news()