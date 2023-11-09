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

def circle_inversion(x, y, circle):
    # circle is a tuple of (x, y, radius)
    # return the inverted point
    dist = math.sqrt((x - circle[0]) ** 2 + (y - circle[1]) ** 2)
    if dist == 0:
        return (x, y)
    else:
        return (circle[0] + (circle[0] - x) / dist * circle[2] ** 2, circle[1] + (circle[1] - y) / dist * circle[2] ** 2)
    
def draw_circle(draw, x, y, radius, color):
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    
    
def draw_fractal(draw, x, y, radius, depth, color, main_circles):
    if depth == 0:
        draw_circle(draw, x, y, radius, color)
    else:
        for i in range(num_main_circles):
            new_x, new_y = circle_inversion(x, y, main_circles[i])
            draw_fractal(draw, new_x, new_y, radius / 2, depth - 1, color, main_circles)
            
def main():
    main_circles = []
    for i in range(num_main_circles):
        main_circles.append((random.randint(0, dimx), random.randint(0, dimy), main_circle_radius))
    img = Image.new('RGB', (dimx, dimy), color = 'white')
    draw = ImageDraw.Draw(img)
    for i in tqdm(range(dimx)):
        for j in range(dimy):
            draw_fractal(draw, i, j, main_circle_radius, max_depth, 'black', main_circles)
    img.show()
    
if __name__ == '__main__':
    main()