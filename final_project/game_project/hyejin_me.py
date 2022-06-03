# pygame 선언
import pygame
import time
import sys

# pygame 초기화(init)
pygame.init()

## pygame에 음악넣기
pygame.mixer.music.load("pygame_bgm.mp3")
pygame.mixer.music.play(0)

# pygame 게임창 옵션 설정
size = [1400, 800]
# W = 1400
# H = 800
screen = pygame.display.set_mode(size)

title = "game"
pygame.display.set_caption(title)

# 게임내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

col_spd =1
col_dir =[1,1,1]
def_col =[0, 0, 0]

font = pygame.font.Font("fonts/Galmuri11.ttf", 30)
font2 = pygame.font.Font("fonts/Galmuri11.ttf", 50)
cr = pygame.image.load("image/circle.png")
pygame.mouse.set_visible(False)


class Obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0
        self.img = None

    def put_img(self, address):
        if address[-3] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))


pb = Obj()
pb.put_img("image/problem.png")
pb.change_size(1200, 700)
pb.x = round(size[0] / 2 - pb.sx / 2)
pb.y = round(size[1] - pb.sy - 5)

har = Obj()
har.put_img("image/heart.png")
har.change_size(80, 80)
har.x = round(size[0] / 2 + 480 + har.sx)
har.y = round(size[1] / 2 - 350)

har2 = Obj()
har2.put_img("image/heart.png")
har2.change_size(80, 80)
har2.x = round(size[0] / 2 + 420 + har.sx)
har2.y = round(size[1] / 2 - 350)

har3 = Obj()
har3.put_img("image/heart.png")
har3.change_size(80, 80)
har3.x = round(size[0] / 2 + 360 + har.sx)
har3.y = round(size[1] / 2 - 350)




# 게임시작화면

def draw_text(font_name, text, size, color, x, y):
    ft = pygame.font.Font(font_name, size)
    text_surface = ft.render(text, True, color)
    # text_rect = text_surface.get_rect()
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)



def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYUP:
                waiting = False
        screen.fill(black)
        draw_text("fonts/Galmuri11.ttf", "*틀린그림찾기*", 100, white, 350, 200)
        draw_text("fonts/Galmuri11.ttf", "~press any key~", 50, def_col, 475, 450)
        col_change(def_col, col_dir)
        clock.tick()
        pygame.display.update()



def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= 255:
            col[i] = 0
        elif col[i] <= 0:
            col[i] =255

# def start_screen_show():
#     screen.fill(black)
#     draw_text("fonts/Galmuri11.ttf", "*틀린그림찾기*", 100, white, 350, 200)
#     draw_text("fonts/Galmuri11.ttf", "~press any key~", 50, def_col, 475, 450)
#     col_change(def_col, col_dir)
#     pygame.display.flip()

wait_for_key()



# pygame 메인루프(이벤트)
st = 0
answer_circle = []
ans = 6
tt = 5


def check_circle(new, answers):
    for c in answers:
        if new.x == c.x and new.y == c.y:
            return False
    return True


while st == 0:
    # (그리기)화면설정
    # 그림띄우기
    screen.fill(black)
    pb.show()
    # 마우스설정
    sor = pygame.mouse.get_pos()
    cou1 = Obj()
    cou1.put_img("image/cousors.png")
    cou1.change_size(35, 35)
    cou1.x = sor[0]
    cou1.y = sor[1]
    cou1.show()

    # 스테이지
    draw_text("fonts/Galmuri11.ttf", "stage 1", 50, white, 60, 5)

    # 하트띄우기
    har.show()
    har2.show()
    har3.show()
    # 갯수
    draw_text("fonts/Galmuri11.ttf", "남은 개수 :" + str(tt), 30, white, 200, 100)

    # 입력 감지(마우스)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()
            print(a)
            if 127 <= a[0] <= 167 and 533 <= a[1] <= 613 or 685 <= a[0] <= 765 and 497 <= a[1] <= 577:
                cir = Obj()
                cir.put_img("image/circle.png")
                cir.change_size(80, 80)
                cir.x = 107
                cir.y = 503
                cir.show()


                cir2 = Obj()
                cir2.put_img("image/circle.png")
                cir2.change_size(80, 80)
                cir2.x = 700
                cir2.y = 500
                cir2.show()

                if check_circle(cir, answer_circle):
                    answer_circle.append(cir)
                    answer_circle.append(cir2)
                    tt -= 1

            if 519 <= a[0] <= 599 and 168 <= a[1] <= 248 or 1100 <= a[0] <= 1180 and 167 <= a[1] <= 247:
                cir3 = Obj()
                cir3.put_img("image/circle.png")
                cir3.change_size(80, 80)
                cir3.x = 559
                cir3.y = 208
                cir3.show()

                cir4 = Obj()
                cir4.put_img("image/circle.png")
                cir4.change_size(80, 80)
                cir4.x = 1140
                cir4.y = 207
                cir4.show()

                if check_circle(cir3, answer_circle):
                    answer_circle.append(cir3)
                    answer_circle.append(cir4)
                    tt -= 1

        if event.type == pygame.QUIT:
            st = 1

    for cir in answer_circle:
        cir.show()
    # fps 설정
    clock.tick(60)
    # 업데이트
    pygame.display.flip()



# 목숨 다했을때 화면
#def fail_screen_show():
screen.fill(black)
draw_text("fonts/Galmuri11.ttf", "ㅠYou Loseㅠ", 100, white, 350, 200) #(폰트크기,색상, x위치, y위치->반대로)
draw_text("fonts/Galmuri11.ttf", "again?", 50, white, 200, 450)
pygame.display.flip()


#fail_screen_show()

# 다 맞췄을때 화면
#def success_screen_show():
screen.fill(black)
draw_text("fonts/Galmuri11.ttf", "CLEAR!!", 100, white, 500, 200) #(폰트크기,색상, x위치, y위치->반대로)
draw_text("fonts/Galmuri11.ttf", "Next Level->", 50, white, 1000, 600)
pygame.display.flip()


#success_screen_show()





# 게임 종료
pygame.quit()