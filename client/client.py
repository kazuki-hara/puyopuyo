import requests
import random
import json


class User:
    def __init__(self):
        self.username = input('名前を入力してください：')
    
    # サーバーにスコアを送信
    def send_score(self, score):
        try:
            response = requests.post(
                'https://puyopuyo-server.herokuapp.com/api/save/',
                {'username': self.username, 'score':score})
            rank = int(json.loads(response.text)['rank'])
            if rank == 0 or rank == -1:
                message = 'Your score is not ranked...'
            else:
                message = 'Your rank is ' + str(rank) + ' !'
            return message
        except:
            messagae = ''
            return message


# サーバー上のスコアデータを全て削除
def reset():
    response = requests.post(
                'https://puyopuyo-server.herokuapp.com/api/reset/',
                {})
    print(json.loads(response.text)['message'])