# pygame 선언
import pygame
import time
import sys
import random

# pygame 초기화(init)
pygame.init()

# pygame 게임창 옵션 설정
size = [1400, 800]
screen = pygame.display.set_mode(size)

title = "game"
pygame.display.set_caption(title)

# 게임내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font("fonts/Galmuri11.ttf", 30)
font2 = pygame.font.Font("fonts/Galmuri11.ttf", 50)
cr = pygame.image.load("image/circle.png")
pygame.mouse.set_visible(False)


# 이미지 불러오는 클래스( 로드 ,사이즈, 위치) 지정
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

har1 = Obj()
har1.put_img("image/heart.png")
har1.change_size(80, 80)
har1.x = round(size[0] / 2 + 480 + har1.sx)
har1.y = round(size[1] / 2 - 350)

har2 = Obj()
har2.put_img("image/heart.png")
har2.change_size(80, 80)
har2.x = round(size[0] / 2 + 420 + har1.sx)
har2.y = round(size[1] / 2 - 350)

har3 = Obj()
har3.put_img("image/heart.png")
har3.change_size(80, 80)
har3.x = round(size[0] / 2 + 360 + har1.sx)
har3.y = round(size[1] / 2 - 350)


# 게임시작화면

# 텍스트 불러오는 함수
def draw_text(font_name, text, size, color, x, y):
    ft = pygame.font.Font(font_name, size)
    text_surface = ft.render(text, True, color)
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)


# 아무키를 누르면 화면 전환
def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


# 시작화면
def start_screen_show():
    screen.fill(black)
    draw_text("fonts/Galmuri11.ttf", "*틀린그림찾기*", 100, white, 350, 200)
    draw_text("fonts/Galmuri11.ttf", "~press any key~", 50, white, 475, 450)
    pygame.display.flip()
    wait_for_key()


start_screen_show()

# pygame 메인루프(이벤트)
st = 0
answer_circle = []
ans = 6
tt = 4
heart_li = [har1, har2, har3]
nope = 0

# 정답 원 처리
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
    har1.show()
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

            if 145 - 40 <= a[0] <= 145 + 40 or 720 - 40 <= a[0] <= 720 + 40 and 218 - 40 <= a[1] <= 218 + 40:
                cir5 = Obj()
                cir5.put_img("image/circle.png")
                cir5.change_size(80, 80)
                cir5.x = 145
                cir5.y = 218
                cir5.show()

                cir6 = Obj()
                cir6.put_img("image/circle.png")
                cir6.change_size(80, 80)
                cir6.x = 720
                cir6.y = 218
                cir6.show()

                if check_circle(cir5, answer_circle):
                    answer_circle.append(cir5)
                    answer_circle.append(cir6)
                    tt -= 1

            if 414 - 40 <= a[0] <= 414 + 40 or 1003 - 40 <= a[0] <= 1003 + 40 and 300 - 40 <= a[1] <= 300 + 40:
                cir7 = Obj()
                cir7.put_img("image/circle.png")
                cir7.change_size(80, 80)
                cir7.x = 414
                cir7.y = 300
                cir7.show()

                cir8 = Obj()
                cir8.put_img("image/circle.png")
                cir8.change_size(80, 80)
                cir8.x = 1003
                cir8.y = 300
                cir8.show()

                if check_circle(cir7, answer_circle):
                    answer_circle.append(cir7)
                    answer_circle.append(cir8)
                    tt -= 1
            else:
                nope += 1
                if len(heart_li) == 3 and nope == 1:
                    heart_li.remove(har3)
                    har3 = Obj()
                    har3.put_img("image/heart.png")
                    har3.change_size(80, 80)
                    har3.x = -999
                    har3.y = -999
                    har3.show()

                if len(heart_li) == 2 and nope == 2:
                    heart_li.remove(har2)
                    har2 = Obj()
                    har2.put_img("image/heart.png")
                    har2.change_size(80, 80)
                    har2.x = -999
                    har2.y = -999
                    har2.show()

                if len(heart_li) == 1 and nope == 3:
                    heart_li.remove(har1)
                    har1 = Obj()
                    har1.put_img("image/heart.png")
                    har1.change_size(80, 80)
                    har1.x = -999
                    har1.y = -999
                    har1.show()

        if event.type == pygame.QUIT:
            st = 1

    for cir in answer_circle:
        cir.show()
    # fps 설정
    clock.tick(60)

    # 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()