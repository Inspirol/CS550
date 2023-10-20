from PIL import Image, ImageDraw, ImageFilter
import math, random

dimx, dimy = 300, 300

img = Image.new("RGB", (dimx, dimy))

# for x in range(dimx):
#     for y in range(dimy):
#         if x % 2 == 0 and y % 2 == 0:
#             img.putpixel((x, y), (255, 0, 0))
#         else:
#             img.putpixel((x, y), (0, 0, 255))

def streamer(color: tuple = (255, 0,0), start_pos: tuple = (math.floor(dimx / 2), 0), width: int = 1):
    start_x, start_y = start_pos
    current_pos = start_pos
    end = False
    if not end:
        while not end:
            # print(current_pos)
            x, y = current_pos
            if random.randint(0, 100) > 70:
                if y + 1 > dimy -1:
                    end = True
                else: 
                    current_pos = (x, (y + 1))
                    # print(current_pos)
                    img.putpixel(current_pos, color)
            else:
                if random.randint(0,100) > 50:
                    if x + 1 > dimx - 1:
                        end = True
                    else: 
                        current_pos = ((x + 1), y)
                        # print(current_pos)
                        img.putpixel(current_pos, color)
                else:
                    if x - 1 < 0:
                        end = True
                    else: 
                        current_pos = ((x - 1), y)
                        # print(current_pos)
                        img.putpixel(current_pos, color)
            

for i in range(100):
    streamer((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, dimx), 0))
    print(i)


img.show()
