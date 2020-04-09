from model import Stage,ControlPuyo
import pygame
import tkinter
import PySimpleGUI as sg

class Puyo:
    def __init__(self, color, pos_x, pos_y):
        self.color = puyo_color[color-1]
        self.pos_y = pos_y
        self.pos_x = pos_x


# ステージの表示
def show_stage(screen):
    size = (300, 600)
    stage_color = (200, 200, 200)
    stage_image = pygame.Surface(size)
    stage_image.set_alpha(220)
    pygame.draw.rect(stage_image, stage_color, stage_image.get_rect())
    screen.blit(stage_image,(80, 20))


def show_next_puyo_stage(screen):
    size = (50, 100)
    stage_color = (200, 200, 200)
    stage_image1 = pygame.Surface(size)
    stage_image2 = pygame.Surface(size)
    stage_image1.set_alpha(220)
    stage_image2.set_alpha(220)
    pygame.draw.rect(stage_image1, stage_color, stage_image1.get_rect())
    pygame.draw.rect(stage_image2, stage_color, stage_image2.get_rect())
    screen.blit(stage_image1,(395, 25))
    screen.blit(stage_image2,(415, 135))


# フィールドに積まれているぷよを表示
def show_field(screen, stage):
    field = stage.field
    for y in range(13, 1, -1):
        for x in range(6):
            if field[y][x] != 0:
                puyo = Puyo(field[y][x], x, y)
                show_puyo(screen, puyo)


# 落ちてくるプヨを表示
def show_falling_puyo(screen, control_puyo):
    for i in range(len(control_puyo.color)):
        if control_puyo.position[i][1] >= 2:
            puyo = Puyo(control_puyo.color[i], control_puyo.position[i][0], control_puyo.position[i][1])
            show_puyo(screen, puyo)
    



# ぷよの色
puyo_color: int = [[180,0,0],[50,170,50],[10,25,140],[145,116,25]]

#　ぷよの半径
radius = 23


# ぷよ１つ１つの表示とデザイン
def show_puyo(screen, puyo):
    color = puyo.color
    pos_x = puyo.pos_x
    pos_y = puyo.pos_y
    draw_pos_x = 105 + pos_x * 50
    draw_pos_y = 595 - (13- pos_y) * 50
    pygame.draw.circle(screen, color, (draw_pos_x, draw_pos_y), radius)


# 次に落ちてくるぷよを表示
def show_next_puyo(screen, control_puyo, scene):
    if scene == 0:
        next_puyo1_color = control_puyo.color
        next_puyo2_color = control_puyo.next_puyo1_color
    else:
        next_puyo1_color = control_puyo.next_puyo1_color
        next_puyo2_color = control_puyo.next_puyo2_color

    # next_puyo1_color
    pygame.draw.circle(screen, puyo_color[next_puyo1_color[0]-1], (420, 100), 20)
    pygame.draw.circle(screen, puyo_color[next_puyo1_color[1]-1], (420, 50), 20)

    # next_puyo2_color
    pygame.draw.circle(screen, puyo_color[next_puyo2_color[0]-1], (440, 210), 20)
    pygame.draw.circle(screen, puyo_color[next_puyo2_color[1]-1], (440, 160), 20)


# Press SPACE to Start!
def show_start_comment(screen):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Press SPACE to Start!", True, (255,0,0))
    screen.blit(text, (60, 300))


# コンボ数を表示
def show_combo(screen,combo):
    combo_font = pygame.font.SysFont(None, 30)
    combo_text = combo_font.render(str(combo) + ' combo!', True, (255, 0, 0))
    screen.blit(combo_text, (385, 500))


# 右下にスコアを表示
def show_score(screen, score):
    score_title_font = pygame.font.SysFont(None,30)
    score_title_text = score_title_font.render('SCORE', True, (255,0,0))
    screen.blit(score_title_text, (390, 550))
    score_font = pygame.font.SysFont(None, 40)
    score_text = score_font.render(str(score), True, (255, 0,0))
    screen.blit(score_text, (390,570))


# ゲームオーバー時に結果を表示
def show_game_over(screen):
    game_over_font = pygame.font.SysFont(None, 100)
    game_over_text = game_over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(game_over_text, (32,200))








if __name__=="__main__":
    enter_username()