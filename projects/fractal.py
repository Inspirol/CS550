# circle fractal
import math
import random
from PIL import Image, ImageDraw
from tqdm import tqdm

num_main_circles = 3
main_circle_radius = 100
max_depth = 5
dimx = 1000
dimy = 1000

def get_color(depth: int) -> tuple:
    return (0, 0, depth*255/max_depth%255)

def get_circle(x: int, y: int, radius: int) -> tuple:
    return (x-radius, y-radius, x+radius, y+radius)

def get_random_circle(x: int, y: int, radius: int) -> tuple:
    return (x+random.randint(-radius, radius), y+random.randint(-radius, radius), radius)

def invert_circle(circle: tuple, dimx: int, dimy: int) -> tuple:
    return (dimx-circle[2], dimy-circle[3], dimx-circle[0], dimy-circle[1])

def get_fractal(depth: int, circle: tuple, dimx: int, dimy: int) -> Image:
    img = Image.new('RGB', (dimx, dimy))
    draw = ImageDraw.Draw(img)
    if depth == 0:
        draw.ellipse(circle, fill=get_color(depth))
        return img
    else:
        draw.ellipse(circle, fill='white')
        for i in range(num_main_circles):
            new_circle = get_random_circle(*circle)
            img.paste(get_fractal(depth-1, new_circle, dimx, dimy), invert_circle(new_circle, dimx, dimy))
        return img
    

img = get_fractal(max_depth, (dimx//2, dimy//2, main_circle_radius), dimx, dimy)
img.show()