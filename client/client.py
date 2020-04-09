import requests
import random
import json
import PySimpleGUI as sg
class User:
    def __init__(self):
        self.username = self.enter_username()
    

    # ユーザー名の入力
    def enter_username(self):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text('プレイヤー名を入力してください',font=("Helvetica", 15))],
            [sg.InputText('' ,font=("Helvetica", 20), size=(15,1))],
            [sg.Submit(button_text='決定', font=("Helvetica",15), size=(5,1))]
        ]
        window = sg.Window('ぷよぷよ？', layout)
        username = ''
        while True:
            event, values = window.read()
            if event is None:
                print('exit')
                break
            if event == '決定':
                username = values[0]
                break
        window.close()
        return username


    # 結果の表示
    def show_result(self, stage, message):
        sg.theme('Dark Blue 3')
        layout = [
            [sg.Text('あなたのスコアは' + str(stage.score) + 'です',font=("Helvetica", 15))],
            [sg.Text(message ,font=("Helvetica", 15))],
            [sg.Submit(button_text='終了', font=("Helvetica",15), size=(5,1)),sg.Submit(button_text='もう一度', font=("Helvetica",15), size=(7,1))]
        ]
        window = sg.Window('ぷよぷよ？', layout)
        flag = 0
        while True:
            event, values = window.read()
            if event is None or event == '終了':
                break
            if event == 'もう一度':
                flag = 1
                break
        window.close()
        return flag


    # サーバーにスコアを送信
    def send_score(self, score):
        try:
            response = requests.post(
                'https://puyopuyo-server.herokuapp.com/api/save/',
                {'username': self.username, 'score':score})
            rank = int(json.loads(response.text)['rank'])
            if rank == 0 or rank == -1:
                message = '残念ながらランキング外です...'
            else:
                message = + str(rank) + ' 位でした!'
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