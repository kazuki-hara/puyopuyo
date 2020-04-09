from model import *
from view import *
from client import *
import sys

WIDTH = 480
HEIGHT = 640


class Game:
    def __init__(self, debug):
        self.user = User()
        self.stage = Stage()
        self.puyo = ControlPuyo()
        self.fps = 5
        self.scene = 0
        self.message = ''
        self.debug_mode = debug

    
    # 背景のロード
    def load_background_image(self):
        background_image = pygame.image.load('img/background.jpg').convert()
        self.background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


    # 次のフレームでの処理
    def update(self):
        self.fps = 5

        # ぷよが上から落ちてくる
        if self.scene == 1:
            self.puyo.fall_puyo()

        # ぷよを消去する ->　消去したらscene3へ、消去しなかったらscene1へ
        elif self.scene == 2:
            next_scene = self.stage.delete_group()
            self.scene = next_scene
            if self.scene == 1:
                self.stage.combo = 0
                self.stage.all_clear()
                self.puyo.update(self.stage)

        # ぷよが消えた分を下に詰める ->　詰め終わったらscene2へ
        elif self.scene == 3:
            self.stage.fall_puyo()
            self.scene = 2


    # 描写
    def draw(self, screen):
        screen.blit(self.background_image,(0,0))
        show_stage(screen)
        show_next_puyo_stage(screen)
        show_next_puyo(screen, self.puyo, self.scene)
        show_score(screen, self.stage.score)

        if self.scene == 0:
            show_start_comment(screen)
        elif self.scene == 1:
            show_field(screen, self.stage)
            show_falling_puyo(screen, self.puyo)
        elif self.scene == 2 or self.scene == 3:
            show_field(screen, self.stage)
            if self.stage.combo > 0:
                show_combo(screen, self.stage.combo)
        elif self.scene == 4:
            show_game_over(screen)


    # キー入力
    def pushed_key(self, events):
        for event in events:
            if event.type == pygame.QUIT or self.scene == 5:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.scene == 0:
                    if event.key == pygame.K_SPACE:
                        self.scene = 1
                elif self.scene == 1:
                    if event.key == pygame.K_a:
                        self.puyo.turn_left(self.stage)
                    if event.key == pygame.K_d:
                        self.puyo.turn_right(self.stage)
                    if event.key == pygame.K_z:
                        self.puyo.move_left(self.stage)
                    if event.key == pygame.K_c:
                        self.puyo.move_right(self.stage)
                elif self.scene == 4:
                    if event.key == pygame.K_SPACE:
                        self.__init__(self.debug_mode)


    # キー長押し
    def pressed_key(self, pressed_keys):
        if self.scene == 1:
            if pressed_keys[pygame.K_SPACE]:
                self.fps = 10


    # 判定
    def judge(self):
        if self.scene == 1:
            if self.puyo.game_over(self.stage):
                next_scene = 4
                if not self.debug_mode:
                    self.message = self.user.send_score(self.stage.score)
            else:
                next_scene = self.puyo.stop_puyo(self.stage)
            self.scene = next_scene
        elif self.scene == 4:
            flag = self.user.show_result(self.stage, self.message)
            if flag == 0:
                self.scene = 5
            else:
                self.__init__(self.debug_mode)

