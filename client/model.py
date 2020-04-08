import random


class Stage:
    def __init__(self):
        self.field = [
            [0, 0, 0, 0, 0, 0], # 画面外
            [0, 0, 0, 0, 0, 0], # 画面外
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.top_position_list = self.top_position()
        self.score = 0
        self.combo = 0
        self.same_time = 0


    # 座標からぷよの色を取得　& 座標が有効か確認
    def get_color(self, x, y):
        if x >=0 and x <= 5 and y >= 2 and y <= 13:
            color = self.field[y][x]
            return color
        else:
            return -1


    # ぷよ変更
    def change_puyo(self, x, y, color):
        self.field[y][x] = color


    # 4つ繋がっているぷよを全て削除
    def delete_group(self):
        # 削除しなかった場合はscene1に移行
        next_scene = 1
        self.same_time = 0
        for y in range(13, 1, -1):
            for x in range(6):
                if self.counter(x, y) >= 4:
                    self._delete_group(x, y)
                    self.same_time += 1
                    # 削除した場合はscene3に移行(ぷよが消えた分を下に詰める)
                    next_scene = 3
        return next_scene


    # 上下左右で同じ色のぷよを削除
    def _delete_group(self, x, y):
        if self.field[y][x] == 0:
            return
        else:
            color = self.get_color(x, y)
            self.field[y][x] = 0
            if self.get_color(x-1, y) == color:
                self._delete_group(x-1, y)
            if self.get_color(x+1, y) == color:
                self._delete_group(x+1, y)
            if self.get_color(x, y-1) == color:
                self._delete_group(x, y-1)
            if self.get_color(x, y+1) == color:
                self._delete_group(x, y+1)


    # 繋がっている個数を確認
    def counter(self, x, y):
        searched_list = []
        count = self._counter(x, y, searched_list)
        return count


    def _counter(self, x, y, searched_list):
        if self.get_color(x, y) <= 0 or [x, y] in searched_list:
            return 0
        else:
            count = 1
            searched_list.append([x, y])
            color = self.get_color(x, y)
            if self.get_color(x-1, y) == color:
                count += self._counter(x-1, y, searched_list)
            if self.get_color(x+1, y) == color:
                count += self._counter(x+1, y, searched_list)
            if self.get_color(x, y-1) == color:
                count += self._counter(x, y-1, searched_list)
            if self.get_color(x, y+1) == color:
                count += self._counter(x, y+1, searched_list)
            return count


    # ぷよ削除後の落下処理
    def fall_puyo(self):
        self.combo += 1
        self.score += self.combo * 100 + (self.same_time-1) * 50
        while True: 
            if not self._fall_puyo():
                # これ以上、下に詰められなくなったら終了
                break


    # ぷよ削除後の落下処理(1段)
    def _fall_puyo(self):
        flag = False
        for y in range(12, 1, -1):
            for x in range(6):
                color = self.get_color(x, y)
                if color >= 1 and self.get_color(x, y+1) == 0:
                    self.change_puyo(x, y, 0)
                    self.change_puyo(x, y+1, color)
                    flag = True
        return flag


    # 各列の最上段のリストを取得
    def top_position(self):
        top_position_list = []
        for x in range(6):
            pos = 14
            for y in range(13, 1, -1):
                if self.field[y][x] != 0:
                    pos = y
            top_position_list.append(pos - 1)
        return top_position_list

    
    # 全消しボーナス
    def all_clear(self):
        all_clear = True
        for row in self.field:
            for color in row:
                if not color == 0:
                    all_clear = False
        if all_clear == True:
            self.score += 1000
        




class ControlPuyo:
    def __init__(self):
        self.color = [random.randint(1, 4), random.randint(1, 4)]
        self.position = [[2, 1], [2, 0]]
        self.angle = 0 # 縦向き
        self.next_puyo1_color = [random.randint(1, 4), random.randint(1, 4)]
        self.next_puyo2_color = [random.randint(1, 4), random.randint(1, 4)]


    # 毎フレーム0.5個分ずつ落下
    def fall_puyo(self):
        for position in self.position:
            position[1] += 0.5


    # 積まれているぷよの上でストップ
    def stop_puyo(self, stage):
        next_scene = 1
        if len(self.position) == 2 and self.position[0][0] == self.position[1][0]:
            pos_x = self.position[0][0]
            pos_y = max([position[1] for position in self.position])
            if pos_y == stage.top_position_list[pos_x]:
                for i in range(2):
                    pos_x = self.position[i][0]
                    pos_y = self.position[i][1]
                    stage.field[int(pos_y)][int(pos_x)] = self.color[i]
                next_scene = 2
        else:
            for i in range(len(self.position)-1,-1, -1):
                position = self.position[i]
                pos_x = position[0]
                pos_y = position[1]
                if pos_y == stage.top_position_list[pos_x]:
                    stage.field[int(pos_y)][int(pos_x)] = self.color[i]
                    del self.color[i]
                    del self.position[i]
                    stage.top_position_list = stage.top_position()
            if len(self.position) == 0:
                next_scene = 2
        return next_scene


    # 左の列に移動
    def move_left(self, stage):
        if len(self.position) == 2:
            if self.position[0][0] == self.position[1][0]:
                pos_x = self.position[0][0]
                pos_y = max([position[1] for position in self.position])
            else:
                pos_x = min([position[0] for position in self.position])
                pos_y = self.position[0][1]
        elif len(self.position) == 1:
            pos_x = self.position[0][0]
            pos_y = self.position[0][1]

        if not pos_x == 0:
            if pos_y <= stage.top_position_list[pos_x-1]:
                for position in self.position:
                    position[0] -= 1


    # 右の列に移動
    def move_right(self, stage):
        if len(self.position) == 2:
            if self.position[0][0] == self.position[1][0]:
                pos_x = self.position[0][0]
                pos_y = max([position[1] for position in self.position])
            else:
                pos_x = max([position[0] for position in self.position])
                pos_y = self.position[0][1]
        elif len(self.position) == 1:
            pos_x = self.position[0][0]
            pos_y = self.position[0][1]

        if not pos_x == 5:
            if pos_y <= stage.top_position_list[pos_x + 1]:
                for position in self.position:
                    position[0] += 1


    # 左回転
    def turn_left(self, stage):
        if len(self.position) == 2:
            pos_x = self.position[1][0]
            pos_y = self.position[1][1]
            if self.angle == 0 and pos_x != 0:
                if pos_y + 1 <= stage.top_position_list[pos_x-1]:
                    self.position[1][0] = self.position[0][0] - 1  
                    self.position[1][1] = self.position[0][1] 
                    self.angle = 3
            elif self.angle == 3 and pos_y + 1 <= stage.top_position_list[pos_x+1]:
                self.position[1][0] = self.position[0][0] 
                self.position[1][1] = self.position[0][1] + 1
                self.angle = 2
            elif self.angle == 2 and pos_x != 5:
                if pos_y - 1 <= stage.top_position_list[pos_x+1]:
                    self.position[1][0] = self.position[0][0] + 1
                    self.position[1][1] = self.position[0][1]
                    self.angle = 1
            elif self.angle == 1:
                self.position[1][0] = self.position[0][0]
                self.position[1][1] = self.position[0][1] - 1
                self.angle = 0


    # 右回転
    def turn_right(self, stage):
        if len(self.position) == 2:
            pos_x = self.position[1][0]
            pos_y = self.position[1][1]
            if self.angle == 0 and pos_x != 5:
                if pos_y + 1 <= stage.top_position_list[pos_x+1]:
                    self.position[1][0] = self.position[0][0] + 1  
                    self.position[1][1] = self.position[0][1]
                    self.angle = 1
            elif self.angle == 1 and pos_y + 1 <= stage.top_position_list[pos_x-1]:
                self.position[1][0] = self.position[0][0] 
                self.position[1][1] = self.position[0][1] + 1
                self.angle = 2
            elif self.angle == 2 and pos_x != 0:
                if pos_y - 1 <= stage.top_position_list[pos_x-1]:
                    self.position[1][0] = self.position[0][0] - 1
                    self.position[1][1] = self.position[0][1]
                    self.angle = 3
            elif self.angle == 3:
                self.position[1][0] = self.position[0][0]
                self.position[1][1] = self.position[0][1] - 1
                self.angle = 0


    # 次のぷよになったら更新
    def update(self, stage):
        stage.combo = 0
        self.color = self.next_puyo1_color
        self.position = [[2, 1], [2, 0]]
        self.next_puyo1_color = self.next_puyo2_color
        self.next_puyo2_color = [random.randint(1, 4), random.randint(1, 4)]
    

    # ゲームオーバー
    def game_over(self, stage):
        stage.top_position_list = stage.top_position()
        if stage.top_position_list[2] < 2:
            return True
        else:
            return False


class NextPuyo:
    def __init__(self):
        self.next_puyo1 = [random.randint(1,4), random.randint(1,4)]
        self.next_puyo2 = [random.randint(1,4), random.randint(1,4)]

    def update(self):
        self.next_puyo1 = self.next_puyo2
        self.next_puyo2 = [random.randint(1,4), random.randint(1,4)]