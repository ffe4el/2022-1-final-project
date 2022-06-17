# pygame 선언
import pygame
import sys

# pygame 초기화(init)
pygame.init()

# pygame 게임창 옵션 설정
size = [1400, 800]
screen = pygame.display.set_mode(size)

title = "game"
pygame.display.set_caption(title)

# pygame에 음악넣기
pygame.mixer.music.load("bgm/pygame_bgm.mp3")
pygame.mixer.music.play(0)

# 게임내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font("fonts/Galmuri11.ttf", 30)
font2 = pygame.font.Font("fonts/Galmuri11.ttf", 50)
pygame.mouse.set_visible(False)
yesImg = pygame.image.load("image/yes.png")
noImg = pygame.image.load("image/no.png")
pygame.transform.scale(yesImg, (90, 130))
pygame.transform.scale(noImg, (90, 130))
mySound = pygame.mixer.Sound("bgm/answer.wav")
wr_sound = pygame.mixer.Sound("bgm/worng.wav")
compl = pygame.mixer.Sound("bgm/clear.wav")
loser = pygame.mixer.Sound("bgm/lose.mp3")
cong = pygame.mixer.Sound("bgm/yeah.mp3")
mySound.set_volume(1.0)
wr_sound.set_volume(1.0)


col_spd = 5
col_dir = [1, 1, 1]
def_col = [0, 0, 0]


# 종료 함수
def quitgame():
    pygame.quit()
    sys.exit()


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

pb2 = Obj()
pb2.put_img("image/pb2.png")
pb2.change_size(1200, 620)
pb2.x = round(size[0] / 2 - pb.sx / 2)
pb2.y = round(size[1] - pb.sy + 40)

pb4 = Obj()
pb4.put_img("image/pb3-removebg-preview.png")
pb4.change_size(1200, 700)
pb4.x = round(size[0] / 2 - pb.sx / 2)
pb4.y = round(size[1] - pb.sy - 5)

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


# 텍스트 불러오는 함수
def draw_text(font_name, text, size, color, x, y):
    ft = pygame.font.Font(font_name, size)
    text_surface = ft.render(text, True, color)
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)



# 게임시작화면
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYUP:
                waiting = False
        screen.fill(black)
        retro = Obj()
        retro.put_img("image/retro.png")
        retro.change_size(310, 310)
        retro.x = 525
        retro.y = 305
        retro.show()
        draw_text("fonts/Galmuri11-Bold.ttf", "# 틀린그림찾기 #", 100, white, 300, 150)
        draw_text("fonts/Galmuri11.ttf", "~press any key~", 50, def_col, 470, 600)
        col_change(def_col, col_dir)
        clock.tick(60)
        pygame.display.update()

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= 255:
            col[i] = 0
        elif col[i] <= 0:
            col[i] = 255


wait_for_key()

# 게임 내 이벤트
st = 0
answer_circle = []
answer_circle2 = []
answer_circle3 = []
total_score = []
all_total_score = []
ans = 6
tt = 5
nope = 0
heart_li = [har1, har2, har3]
total_time = 181
start_ticks = pygame.time.get_ticks()


# 정답 원 처리
def check_circle(new, answers):
    for c in answers:
        if new.x == c.x and new.y == c.y:
            return False
    return True


# 목숨 다했을때 화면
def fail_screen_show():
    global start_ticks
    waiting = True
    pygame.mixer.music.pause()
    loser.play()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            screen.fill(black)
            draw_text("fonts/Galmuri11.ttf", "ㅠYou Loseㅠ", 100, white, 350, 200)  # (폰트크기,색상, x위치, y위치->반대로)
            draw_text("fonts/Galmuri11.ttf", "again?", 50, white, 200, 450)
            yes = Obj()
            yes.put_img("image/yes.png")
            yes.change_size(210, 190)
            yes.x = 500
            yes.y = 400
            yes.show()

            no = Obj()
            no.put_img("image/no.png")
            no.change_size(190, 160)
            no.x = 850
            no.y = 415
            no.show()

            sor = pygame.mouse.get_pos()

            if 640 - 150 < sor[0] < 640 + 150 and 480 - 60 < sor[1] < 480 + 60:
                yes = Obj()
                yes.put_img("image/yes.png")
                yes.change_size(230, 210)
                yes.x = 490
                yes.y = 395
                yes.show()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 640 - 150 < sor[0] < 640 + 150 and 480 - 60 < sor[1] < 480 + 60:
                        waiting = False
                        pygame.mixer.music.unpause()
                        start_ticks = pygame.time.get_ticks()

            if 1000 - 150 < sor[0] < 1000 + 150 and 480 - 60 < sor[1] < 480 + 60:
                no = Obj()
                no.put_img("image/no.png")
                no.change_size(210, 180)
                no.x = 840
                no.y = 410
                no.show()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 1000 - 150 < sor[0] < 1000 + 150 and 480 - 60 < sor[1] < 480 + 60:
                        quitgame()

            cou1 = Obj()
            cou1.put_img("image/cousors.png")
            cou1.change_size(35, 35)
            cou1.x = sor[0]
            cou1.y = sor[1]
            cou1.show()

            pygame.display.flip()


# 다 맞췄을때 화면
def success_screen_show():
    waiting = True
    pygame.mixer.music.pause()
    compl.play()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYUP:
                waiting = False
            if event.type == pygame.MOUSEBUTTONUP:
                waiting = False
            screen.fill(black)
            draw_text("fonts/Galmuri11-Bold.ttf", "CLEAR!!", 180, (255, 204, 204), 400, 180)
            draw_text("fonts/Galmuri11.ttf", "Next Level->", 50, white, 1000, 600)
            draw_text("fonts/Galmuri11.ttf", "Enter!", 50, (255,0,0), 1070, 530)

            homer = Obj()
            homer.put_img("image/homer.png")
            homer.change_size(400, 400)
            homer.x = 0
            homer.y = 400
            homer.show()
            pygame.display.flip()


#진짜 마지막 화면
def real_final():
    score = sum(total_score)
    global start_ticks
    global nope
    waiting = True
    pygame.mixer.music.unpause()
    cong.play()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            screen.fill(black)
            draw_text("fonts/Galmuri11.ttf", "CLEAR!!", 100, white, 500, 200)  # (폰트크기,색상, x위치, y위치->반대로)
            draw_text("fonts/Galmuri11.ttf", "your score :" + str(score), 80, white, 380, 400)
            draw_text("fonts/Galmuri11.ttf", "again?", 50, white, 200, 600)

            con = Obj()
            con.put_img("image/cong.png")
            con.change_size(350, 350)
            con.x = 100
            con.y = 100
            con.show()

            con2 = Obj()
            con2.put_img("image/cong.png")
            con2.change_size(350, 350)
            con2.x = 950
            con2.y = 100
            con2.show()

            yes = Obj()
            yes.put_img("image/yes.png")
            yes.change_size(180, 160)
            yes.x = 500
            yes.y = 550
            yes.show()

            no = Obj()
            no.put_img("image/no.png")
            no.change_size(160, 130)
            no.x = 800
            no.y = 565
            no.show()

            sor = pygame.mouse.get_pos()

            if 540 - 150 < sor[0] < 540 + 150 and 590 - 60 < sor[1] < 590 + 60:
                yes = Obj()
                yes.put_img("image/yes.png")
                yes.change_size(200, 180)
                yes.x = 490
                yes.y = 545
                yes.show()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 540 - 150 < sor[0] < 540 + 150 and 590 - 60 < sor[1] < 590 + 60:
                        waiting = False

                        har1.x = round(size[0] / 2 + 480 + har1.sx)
                        har1.y = round(size[1] / 2 - 350)

                        har2.x = round(size[0] / 2 + 420 + har1.sx)
                        har2.y = round(size[1] / 2 - 350)

                        har3.x = round(size[0] / 2 + 360 + har1.sx)
                        har3.y = round(size[1] / 2 - 350)

                        nope = 0
                        if len(heart_li) == 1:
                            heart_li.append(har2)
                            heart_li.append(har3)
                        elif len(heart_li) == 2:
                            heart_li.append(har3)

                        answer_circle.clear()
                        answer_circle2.clear()
                        answer_circle3.clear()
                        total_score.clear()
                        start_ticks = pygame.time.get_ticks()

            if 840 - 150 < sor[0] < 840 + 150 and 605 - 60 < sor[1] < 605 + 60:
                no = Obj()
                no.put_img("image/no.png")
                no.change_size(180, 150)
                no.x = 790
                no.y = 560
                no.show()
                if event.type == pygame.MOUSEBUTTONUP:
                    if 840 - 150 < sor[0] < 840 + 150 and 605 - 60 < sor[1] < 605 + 60:
                        quitgame()

            cou1 = Obj()
            cou1.put_img("image/cousors.png")
            cou1.change_size(35, 35)
            cou1.x = sor[0]
            cou1.y = sor[1]
            cou1.show()

        clock.tick(60)
        total_score.clear()
        pygame.display.flip()


# 스테이지2
def stage2():
    global har1, har2, har3
    global tt
    global total_time
    pygame.mixer.music.unpause()
    total_time2 = 121
    start_ticks2 = pygame.time.get_ticks()
    tt = 5
    uu = 10
    waiting = True
    while waiting:
        screen.fill(black)
        pb2.show()

        draw_text("fonts/Galmuri11.ttf", "stage 2", 50, white, 60, 5)

        har1.show()
        har2.show()
        har3.show()

        draw_text("fonts/Galmuri11.ttf", "남은 개수 :" + str(uu), 30, white, 200, 100)

        seconds2 = (pygame.time.get_ticks() - start_ticks2) / 1000  # calculate how many seconds
        min2, sec2 = divmod(int(total_time2 - seconds2), 60)
        ti_mer2 = font2.render("{:02d}:{:02d}".format(min2, sec2), True, white)
        screen.blit(ti_mer2, (630, 10))

        sor = pygame.mouse.get_pos()
        cou1 = Obj()
        cou1.put_img("image/cousors.png")
        cou1.change_size(35, 35)
        cou1.x = sor[0]
        cou1.y = sor[1]
        cou1.show()

        if int(total_time2 - seconds2) == 0:
            fail_screen_show()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                p = pygame.mouse.get_pos()
                if 107 <= p[0] <= 233 and 147 <= p[1] <= 229 or 714 <= p[0] <= 844 and 147 <= p[1] <= 229:
                    mySound.play()
                    cir = Obj()
                    cir.put_img("image/123.png")
                    cir.change_size(80, 80)
                    cir.x = 128
                    cir.y = 155
                    cir.show()

                    cir2 = Obj()
                    cir2.put_img("image/123.png")
                    cir2.change_size(80, 80)
                    cir2.x = 746
                    cir2.y = 162
                    cir2.show()

                    if check_circle(cir, answer_circle2):
                        answer_circle2.append(cir)
                        answer_circle2.append(cir2)
                        uu -= 1

                elif 753 - 40 <= p[0] <= 753 + 40 and 620 - 40 <= p[1] <= 620 + 40 or 143 - 40 <= p[
                    0] <= 143 + 40 and 620 - 40 <= p[1] <= 620 + 40:
                    mySound.play()
                    cir3 = Obj()
                    cir3.put_img("image/123.png")
                    cir3.change_size(80, 80)
                    cir3.x = 713
                    cir3.y = 580
                    cir3.show()

                    cir4 = Obj()
                    cir4.put_img("image/123.png")
                    cir4.change_size(80, 80)
                    cir4.x = 103
                    cir4.y = 580
                    cir4.show()

                    if check_circle(cir3, answer_circle2):
                        answer_circle2.append(cir3)
                        answer_circle2.append(cir4)
                        uu -= 1

                elif 188 - 40 <= p[0] <= 188 + 40 and 410 - 40 <= p[1] <= 410 + 40 or 804 - 40 <= p[
                    0] <= 804 + 40 and 410 - 40 <= p[1] <= 410 + 40:
                    mySound.play()
                    cir5 = Obj()
                    cir5.put_img("image/123.png")
                    cir5.change_size(80, 80)
                    cir5.x = 148
                    cir5.y = 370
                    cir5.show()

                    cir6 = Obj()
                    cir6.put_img("image/123.png")
                    cir6.change_size(80, 80)
                    cir6.x = 764
                    cir6.y = 370
                    cir6.show()

                    if check_circle(cir5, answer_circle2):
                        answer_circle2.append(cir5)
                        answer_circle2.append(cir6)
                        uu -= 1

                elif 485 - 40 <= p[0] <= 485 + 40 and 173 - 40 <= p[1] <= 173 + 40 or 1091 - 40 <= p[
                    0] <= 1091 + 40 and 173 - 40 <= p[1] <= 173 + 40:
                    mySound.play()
                    cir7 = Obj()
                    cir7.put_img("image/123.png")
                    cir7.change_size(80, 80)
                    cir7.x = 445
                    cir7.y = 133
                    cir7.show()

                    cir8 = Obj()
                    cir8.put_img("image/123.png")
                    cir8.change_size(80, 80)
                    cir8.x = 1051
                    cir8.y = 133
                    cir8.show()

                    if check_circle(cir7, answer_circle2):
                        answer_circle2.append(cir7)
                        answer_circle2.append(cir8)
                        uu -= 1

                elif 547 - 40 <= p[0] <= 547 + 40 and 352 - 40 <= p[1] <= 352 + 40 or 1164 - 40 <= p[
                    0] <= 1164 + 40 and 352 - 40 <= p[1] <= 352 + 40:
                    mySound.play()
                    cir9 = Obj()
                    cir9.put_img("image/123.png")
                    cir9.change_size(80, 80)
                    cir9.x = 507
                    cir9.y = 312
                    cir9.show()

                    cir10 = Obj()
                    cir10.put_img("image/123.png")
                    cir10.change_size(80, 80)
                    cir10.x = 1124
                    cir10.y = 304
                    cir10.show()

                    if check_circle(cir9, answer_circle2):
                        answer_circle2.append(cir9)
                        answer_circle2.append(cir10)
                        uu -= 1

                elif 535 - 40 <= p[0] <= 535 + 40 and 700 - 40 <= p[1] <= 700 + 40 or 1133 - 40 <= p[
                    0] <= 1133 + 40 and 700 - 40 <= p[1] <= 700 + 40:
                    mySound.play()
                    cir11 = Obj()
                    cir11.put_img("image/123.png")
                    cir11.change_size(80, 80)
                    cir11.x = 495
                    cir11.y = 660
                    cir11.show()

                    cir12 = Obj()
                    cir12.put_img("image/123.png")
                    cir12.change_size(80, 80)
                    cir12.x = 1093
                    cir12.y = 660
                    cir12.show()

                    if check_circle(cir11, answer_circle2):
                        answer_circle2.append(cir11)
                        answer_circle2.append(cir12)
                        uu -= 1

                elif 623 - 40 < p[0] <= 623 + 40 and 330 - 40 <= p[1] <= 330 + 40 or 1246 - 40 <= p[
                    0] <= 1246 + 40 and 330 - 40 <= p[1] <= 330 + 40:
                    mySound.play()
                    cir13 = Obj()
                    cir13.put_img("image/123.png")
                    cir13.change_size(80, 80)
                    cir13.x = 583
                    cir13.y = 290
                    cir13.show()

                    cir14 = Obj()
                    cir14.put_img("image/123.png")
                    cir14.change_size(80, 80)
                    cir14.x = 1206
                    cir14.y = 290
                    cir14.show()

                    if check_circle(cir13, answer_circle2):
                        answer_circle2.append(cir13)
                        answer_circle2.append(cir14)
                        uu -= 1

                elif 352 - 40 <= p[0] <= 462 + 40 and 460 - 40 <= p[1] <= 460 + 40 or 962 - 40 <= p[0] <= 962 + 40 \
                        and 460 - 40 <= p[1] <= 460 + 40:
                    mySound.play()
                    cir15 = Obj()
                    cir15.put_img("image/123.png")
                    cir15.change_size(80, 80)
                    cir15.x = 312
                    cir15.y = 420
                    cir15.show()

                    cir16 = Obj()
                    cir16.put_img("image/123.png")
                    cir16.change_size(80, 80)
                    cir16.x = 922
                    cir16.y = 420
                    cir16.show()

                    if check_circle(cir15, answer_circle2):
                        answer_circle2.append(cir15)
                        answer_circle2.append(cir16)
                        uu -= 1

                elif 1128 - 40 <= p[0] <= 1128 + 40 and 490 - 40 <= p[1] <= 490 + 40 or 533 - 40 <= p[
                    0] <= 533 + 40 and 490 - 40 <= p[1] <= 490 + 40:
                    mySound.play()
                    cir17 = Obj()
                    cir17.put_img("image/123.png")
                    cir17.change_size(80, 80)
                    cir17.x = 1088
                    cir17.y = 450
                    cir17.show()

                    cir18 = Obj()
                    cir18.put_img("image/123.png")
                    cir18.change_size(80, 80)
                    cir18.x = 513
                    cir18.y = 450
                    cir18.show()

                    if check_circle(cir17, answer_circle2):
                        answer_circle2.append(cir17)
                        answer_circle2.append(cir18)
                        uu -= 1

                elif 886 - 40 <= p[0] <= 886 + 40 and 712 - 40 <= p[1] <= 712 + 40 or 282 - 40 <= p[
                    0] <= 282 + 40 and 712 - 40 <= p[1] <= 712 + 40:
                    mySound.play()
                    cir19 = Obj()
                    cir19.put_img("image/123.png")
                    cir19.change_size(80, 80)
                    cir19.x = 846
                    cir19.y = 672
                    cir19.show()

                    cir20 = Obj()
                    cir20.put_img("image/123.png")
                    cir20.change_size(80, 80)
                    cir20.x = 246
                    cir20.y = 672
                    cir20.show()

                    if check_circle(cir19, answer_circle2):
                        answer_circle2.append(cir19)
                        answer_circle2.append(cir20)
                        uu -= 1
                else:
                    wr_sound.play()
                    if len(heart_li) == 3:
                        heart_li.remove(har3)
                        har3 = Obj()
                        har3.put_img("image/heart.png")
                        har3.change_size(80, 80)
                        har3.x = -999
                        har3.y = -999
                        har3.show()

                    elif len(heart_li) == 2:
                        heart_li.remove(har2)
                        har2 = Obj()
                        har2.put_img("image/heart.png")
                        har2.change_size(80, 80)
                        har2.x = -999
                        har2.y = -999
                        har2.show()

                    elif len(heart_li) == 1:
                        heart_li.remove(har1)
                        har1 = Obj()
                        har1.put_img("image/heart.png")
                        har1.change_size(80, 80)
                        har1.x = -999
                        har1.y = -999
                        har1.show()

                        waiting = False
                        fail_screen_show()
                        har1.x = round(size[0] / 2 + 480 + har1.sx)
                        har1.y = round(size[1] / 2 - 350)

                        har2.x = round(size[0] / 2 + 420 + har1.sx)
                        har2.y = round(size[1] / 2 - 350)

                        har3.x = round(size[0] / 2 + 360 + har1.sx)
                        har3.y = round(size[1] / 2 - 350)

                        heart_li.append(har1)
                        heart_li.append(har2)
                        heart_li.append(har3)
                        answer_circle.clear()
                        answer_circle2.clear()
                        total_score.clear()
                        tt = 5
                        total_time = 181

                if uu == 0:
                    waiting = False
                    success_screen_show()
                    total_score.append(int(total_time2 - seconds2))
                    stage3()

            if event.type == pygame.QUIT:
                quitgame()

        for cir in answer_circle2:
            cir.show()
        clock.tick(60)
        pygame.display.flip()


# 스테이지3
def stage3():
    global har1, har2, har3
    global tt, uu
    pygame.mixer.music.unpause()
    total_time3 = 61
    start_ticks3 = pygame.time.get_ticks()
    oo = 5
    tt = 5
    uu = 10
    waiting = True
    while waiting:
        screen.fill(black)
        pb4.show()

        draw_text("fonts/Galmuri11.ttf", "stage 3", 50, white, 60, 5)

        har1.show()
        har2.show()
        har3.show()

        draw_text("fonts/Galmuri11.ttf", "남은 개수 :" + str(oo), 30, white, 200, 100)

        seconds3 = (pygame.time.get_ticks() - start_ticks3) / 1000  # calculate how many seconds
        min3, sec3 = divmod(int(total_time3 - seconds3), 60)
        ti_mer3 = font2.render("{:02d}:{:02d}".format(min3, sec3), True, white)
        screen.blit(ti_mer3, (630, 10))

        sor = pygame.mouse.get_pos()
        cou1 = Obj()
        cou1.put_img("image/cousors.png")
        cou1.change_size(35, 35)
        cou1.x = sor[0]
        cou1.y = sor[1]
        cou1.show()

        if int(total_time3 - seconds3) == 0:
            fail_screen_show()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                p = pygame.mouse.get_pos()
                if 314 - 40 <= p[0] <= 314 + 40 and 570 - 40 <= p[1] <= 570 + 40 or 873 - 40 <= p[
                    0] <= 873 + 40 and 570 - 40 <= p[1] <= 570 + 40:
                    mySound.play()
                    cr = Obj()
                    cr.put_img("image/123.png")
                    cr.change_size(80, 80)
                    cr.x = 274
                    cr.y = 530
                    cr.show()

                    cr2 = Obj()
                    cr2.put_img("image/123.png")
                    cr2.change_size(80, 80)
                    cr2.x = 833
                    cr2.y = 530
                    cr2.show()

                    if check_circle(cr, answer_circle3):
                        answer_circle3.append(cr)
                        answer_circle3.append(cr2)
                        oo -= 1

                elif 631 - 40 <= p[0] <= 631 + 40 and 656 - 40 <= p[1] <= 656 + 40 or 1188 - 40 <= p[0] <= 1188 + 40 \
                        and 656 - 40 <= p[1] <= 656 + 40:
                    mySound.play()
                    cr3 = Obj()
                    cr3.put_img("image/123.png")
                    cr3.change_size(80, 80)
                    cr3.x = 591
                    cr3.y = 616
                    cr3.show()

                    cr4 = Obj()
                    cr4.put_img("image/123.png")
                    cr4.change_size(80, 80)
                    cr4.x = 1148
                    cr4.y = 616
                    cr4.show()

                    if check_circle(cr3, answer_circle3):
                        answer_circle3.append(cr3)
                        answer_circle3.append(cr4)
                        oo -= 1

                elif 443 - 40 <= p[0] <= 443 + 40 and 185 - 40 <= p[1] <= 185 + 40 or 1000 - 40 <= p[0] <= 1100 + 40 \
                        and 185 - 40 <= p[1] <= 185 + 40:
                    mySound.play()
                    cr5 = Obj()
                    cr5.put_img("image/123.png")
                    cr5.change_size(80, 80)
                    cr5.x = 403
                    cr5.y = 145
                    cr5.show()

                    cr6 = Obj()
                    cr6.put_img("image/123.png")
                    cr6.change_size(80, 80)
                    cr6.x = 960
                    cr6.y = 145
                    cr6.show()

                    if check_circle(cr5, answer_circle3):
                        answer_circle3.append(cr5)
                        answer_circle3.append(cr6)
                        oo -= 1

                elif 548 - 40 <= p[0] <= 548 + 40 and 375 - 40 <= p[1] <= 375 + 40 or 1104 - 40 <= p[0] <= 1104 + 40 \
                        and 375 - 40 <= p[1] <= 375 + 40:
                    mySound.play()
                    cr7 = Obj()
                    cr7.put_img("image/123.png")
                    cr7.change_size(80, 80)
                    cr7.x = 508
                    cr7.y = 335
                    cr7.show()

                    cr8 = Obj()
                    cr8.put_img("image/123.png")
                    cr8.change_size(80, 80)
                    cr8.x = 1064
                    cr8.y = 335
                    cr8.show()

                    if check_circle(cr7, answer_circle3):
                        answer_circle3.append(cr7)
                        answer_circle3.append(cr8)
                        oo -= 1

                elif 239 - 40 <= p[0] <= 239 + 40 and 300 - 40 <= p[1] <= 300 + 40 or 796 - 40 <= p[0] <= 796 + 40 \
                        and 300 - 40 <= p[1] <= 300 + 40:
                    mySound.play()
                    cr9 = Obj()
                    cr9.put_img("image/123.png")
                    cr9.change_size(80, 80)
                    cr9.x = 199
                    cr9.y = 260
                    cr9.show()

                    cr10 = Obj()
                    cr10.put_img("image/123.png")
                    cr10.change_size(80, 80)
                    cr10.x = 756
                    cr10.y = 260
                    cr10.show()

                    if check_circle(cr9, answer_circle3):
                        answer_circle3.append(cr9)
                        answer_circle3.append(cr10)
                        oo -= 1

                else:
                    wr_sound.play()
                    if len(heart_li) == 3:
                        heart_li.remove(har3)
                        har3 = Obj()
                        har3.put_img("image/heart.png")
                        har3.change_size(80, 80)
                        har3.x = -999
                        har3.y = -999
                        har3.show()

                    elif len(heart_li) == 2:
                        heart_li.remove(har2)
                        har2 = Obj()
                        har2.put_img("image/heart.png")
                        har2.change_size(80, 80)
                        har2.x = -999
                        har2.y = -999
                        har2.show()

                    elif len(heart_li) == 1:
                        heart_li.remove(har1)
                        har1 = Obj()
                        har1.put_img("image/heart.png")
                        har1.change_size(80, 80)
                        har1.x = -999
                        har1.y = -999
                        har1.show()
                        fail_screen_show()
                        waiting = False

                        har1.x = round(size[0] / 2 + 480 + har1.sx)
                        har1.y = round(size[1] / 2 - 350)

                        har2.x = round(size[0] / 2 + 420 + har1.sx)
                        har2.y = round(size[1] / 2 - 350)

                        har3.x = round(size[0] / 2 + 360 + har1.sx)
                        har3.y = round(size[1] / 2 - 350)

                        heart_li.append(har1)
                        heart_li.append(har2)
                        heart_li.append(har3)
                        answer_circle.clear()
                        answer_circle2.clear()
                        answer_circle3.clear()
                        total_score.clear()

                if oo == 0:
                    total_score.append(int(total_time3 - seconds3))
                    real_final()
                    waiting = False

            if event.type == pygame.QUIT:
                quitgame()

        for cr in answer_circle3:
            cr.show()
        clock.tick(60)
        pygame.display.flip()


# 게임메인루프
while st == 0:
    # (그리기)화면설정
    # 그림띄우기
    screen.fill(black)
    pb.show()

    # 스테이지
    draw_text("fonts/Galmuri11.ttf", "stage 1", 50, white, 60, 5)

    # 하트띄우기

    har1.show()
    har2.show()
    har3.show()

    # 갯수
    draw_text("fonts/Galmuri11.ttf", "남은 개수 :" + str(tt), 30, white, 200, 100)

    # 마우스설정
    sor = pygame.mouse.get_pos()
    cou1 = Obj()
    cou1.put_img("image/cousors.png")
    cou1.change_size(35, 35)
    cou1.x = sor[0]
    cou1.y = sor[1]
    cou1.show()

    # 시간
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    min, sec = divmod(int(total_time - seconds), 60)
    ti_mer = font2.render("{:02d}:{:02d}".format(min, sec), True, white)
    screen.blit(ti_mer, (630, 10))

    if int(total_time - seconds) == 0:
        fail_screen_show()

    # 입력 감지(마우스)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            a = pygame.mouse.get_pos()
            if 140 - 40 <= a[0] <= 140 + 40 and 540 - 40 <= a[1] <= 540 + 40 or 732 - 40 <= a[0] <= 732 + 40 \
                and 540 - 40 <= a[1] <= 540 + 40:
                mySound.play()
                cir = Obj()
                cir.put_img("image/123.png")
                cir.change_size(80, 80)
                cir.x = 112
                cir.y = 500
                cir.show()

                cir2 = Obj()
                cir2.put_img("image/123.png")
                cir2.change_size(80, 80)
                cir2.x = 700
                cir2.y = 500
                cir2.show()

                if check_circle(cir, answer_circle):
                    answer_circle.append(cir)
                    answer_circle.append(cir2)
                    tt -= 1

            elif 594 - 40 <= a[0] <= 594 + 40 and 245 - 40 <= a[1] <= 245 + 40 or 1175 - 40 <= a[0] <= 1175 + 40 \
                    and 245 - 40 <= a[1] <= 245 + 40:
                mySound.play()
                cir3 = Obj()
                cir3.put_img("image/123.png")
                cir3.change_size(80, 80)
                cir3.x = 559
                cir3.y = 208
                cir3.show()
                cir4 = Obj()
                cir4.put_img("image/123.png")
                cir4.change_size(80, 80)
                cir4.x = 1140
                cir4.y = 208
                cir4.show()

                if check_circle(cir3, answer_circle):
                    answer_circle.append(cir3)
                    answer_circle.append(cir4)
                    tt -= 1

            elif 184 - 40 <= a[0] <= 184 + 40 and 255 - 40 <= a[1] <= 255 + 40 \
                    or 760 - 40 <= a[0] <= 760 + 40 and 255 - 40 <= a[1] <= 255 + 40:
                mySound.play()
                cir5 = Obj()
                cir5.put_img("image/123.png")
                cir5.change_size(80, 80)
                cir5.x = 150
                cir5.y = 218
                cir5.show()

                cir6 = Obj()
                cir6.put_img("image/123.png")
                cir6.change_size(80, 80)
                cir6.x = 730
                cir6.y = 218
                cir6.show()

                if check_circle(cir5, answer_circle):
                    answer_circle.append(cir5)
                    answer_circle.append(cir6)
                    tt -= 1

            elif 459 - 40 <= a[0] <= 459 + 40 and 330 - 40 <= a[1] <= 330 + 40 or 1036 - 40 <= a[0] <= 1036 + 40 \
                    and 330 - 40 <= a[1] <= 330 + 40:
                mySound.play()
                cir7 = Obj()
                cir7.put_img("image/123.png")
                cir7.change_size(80, 80)
                cir7.x = 420
                cir7.y = 290
                cir7.show()

                cir8 = Obj()
                cir8.put_img("image/123.png")
                cir8.change_size(80, 80)
                cir8.x = 1003
                cir8.y = 290
                cir8.show()

                if check_circle(cir7, answer_circle):
                    answer_circle.append(cir7)
                    answer_circle.append(cir8)
                    tt -= 1

            elif 471 - 40 <= a[0] <= 471 + 40 and 641 - 40 <= a[1] <= 641 + 40 or 1052 - 40 <= a[0] <= 1052 + 40 \
                    and 641 - 40 <= a[1] <= 641 + 40:
                mySound.play()
                cir9 = Obj()
                cir9.put_img("image/123.png")
                cir9.change_size(80, 80)
                cir9.x = 431
                cir9.y = 601
                cir9.show()

                cir10 = Obj()
                cir10.put_img("image/123.png")
                cir10.change_size(80, 80)
                cir10.x = 1012
                cir10.y = 601
                cir10.show()

                if check_circle(cir9, answer_circle):
                    answer_circle.append(cir9)
                    answer_circle.append(cir10)
                    tt -= 1

            else:
                nope += 1
                wr_sound.play()
                if len(heart_li) == 3 and nope % 3 == 1:
                    heart_li.remove(har3)
                    har3 = Obj()
                    har3.put_img("image/heart.png")
                    har3.change_size(80, 80)
                    har3.x = -999
                    har3.y = -999
                    har3.show()

                if len(heart_li) == 2 and nope % 3 == 2:
                    heart_li.remove(har2)
                    har2 = Obj()
                    har2.put_img("image/heart.png")
                    har2.change_size(80, 80)
                    har2.x = -999
                    har2.y = -999
                    har2.show()

                if len(heart_li) == 1 and nope % 3 == 0:
                    heart_li.remove(har1)
                    har1 = Obj()
                    har1.put_img("image/heart.png")
                    har1.change_size(80, 80)
                    har1.x = -999
                    har1.y = -999
                    har1.show()

                if len(heart_li) == 0:
                    fail_screen_show()
                    har1.x = round(size[0] / 2 + 480 + har1.sx)
                    har1.y = round(size[1] / 2 - 350)

                    har2.x = round(size[0] / 2 + 420 + har1.sx)
                    har2.y = round(size[1] / 2 - 350)

                    har3.x = round(size[0] / 2 + 360 + har1.sx)
                    har3.y = round(size[1] / 2 - 350)
                    total_time = 181

                    tt = 5
                    nope = 0
                    heart_li.append(har1)
                    heart_li.append(har2)
                    heart_li.append(har3)
                    answer_circle.clear()

            if tt == 0:
                total_score.append(int(total_time - seconds))
                success_screen_show()
                stage2()

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
