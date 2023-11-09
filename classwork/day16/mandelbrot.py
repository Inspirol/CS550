# mandelbrot calculation: z = z^2 + c

from PIL import Image, ImageDraw, ImageFilter


# c = complex(-0.7, 0.27015)
'''
<limits>
   <xmin>-1.157918133333333321903</xmin>
   <xmax>-1.146372866666666655463</xmax>
   <ymin>0.303844024999999999860</ymin>
   <ymax>0.312502974999999999910</ymax>
</limits>
'''


# xmin, xmax = -1.157918133333333321903, -1.146372866666666655463
# ymin, ymax = 0.303844024999999999860, 0.312502974999999999910

xmin, xmax = -2, 2
ymin, ymax = -2, 2

dimx, dimy = 500, 500

def get_z(c: complex, z: complex = 0, max_iter: int = 1000) -> complex:
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter


def get_color(z: complex, max_iter: int = 100) -> tuple:
    if z < max_iter:
        return (int(z/max_iter*255), 0, 0)
    elif z == max_iter:
        return (255, 255, 255)
    else:
        return (0, 0, 0)
        
    
def get_mandelbrot_zoom(dimx, dimy, x_range, y_range, max_iter=1000):
    img = Image.new('RGB', (dimx, dimy))
    draw = ImageDraw.Draw(img)
    for x in range(dimx):
        cx = x/dimx*(x_range[1]-x_range[0])+x_range[0]
        for y in range(dimy):
            cy = y/dimy*(y_range[1]-y_range[0])+y_range[0]
            c = complex(cx, cy)
            z = get_z(c, max_iter=max_iter)
            color = get_color(z, max_iter=max_iter)
            draw.point((x, y), fill=color)
    return img

            
    
    
def get_mandelbrot(dimx: int, dimy: int, max_iter: int = 100) -> Image:
    img = Image.new('RGB', (dimx, dimy))
    draw = ImageDraw.Draw(img)
    for x in range(dimx):
        for y in range(dimy):
            c = complex(x/dimx*3-2, y/dimy*3-1.5)
            z = get_z(c, max_iter=max_iter)
            color = get_color(z, max_iter=max_iter)
            draw.point((x, y), fill=color)
    return img

mandel = get_mandelbrot_zoom(dimx, dimy, (xmin, xmax), (ymin, ymax), max_iter=100)
mandel.show()



