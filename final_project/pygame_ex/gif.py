import imageio
import os

directory = r'C:/Users/user/Desktop/gif'       #사진디렉토리
file_type = r'png'                             #사진 확장자
save_gif_name= r'Animation'                    #완성 GIF 이름
speed_sec={'duration':0.1}                     #사진 넘기는 시간(초)

images = []
for file_name in os.listdir(directory):
    if file_name.endswith('.{}'.format(file_type)):
        file_path = os.path.join(directory, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('{}/{}.gif'.format(directory, save_gif_name), images, **speed_sec)
