# circle fractal
'''
name: Sebastian Plunkett
date: 11/17/2023
sources: finishthehot for inversion geometry introduction.
reflection: I never want to do geometry again. Ever. The amount of time I have spent validating if my math is correct via desmos
scares me. Through this process, I suprisingly completely understand the math behind the inversion geometry, and I am very proud of that.
I love the colors and how it all came together. This is probably one of my favorite projects I have done. This circle inversion fractal inverts circles around other circles, and then inverts those circles around other circles, and so on. The result is a beautiful fractal that is very pleasing to the eye. I am very proud of this project, and I hope you enjoy it as much as I do.
Something that I added later was the offset feature, as added after review, and I enjoy it, as it lets you see the fractal from different perspectives.
Please have fun tinkering with the class objects! Sorry I could not explain every little detail of the code, as it is technically dificult to explain, but I hope you enjoy it!
Honor Code: I have not given nor received any unauthorized aid on this assignment. -Sebastian Plunkett
'''

import math
import random
from PIL import Image, ImageDraw
from tqdm import tqdm

num_main_circles = 3
main_circle_radius = 100
max_depth = 20
dimx = 4000
dimy = 4000


class Mandelbrot():
    '''
    creates a mandelbrot set'''

    def get_z(self, c: complex, z: complex = 0, max_iter: int = 1000) -> complex:
        for i in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                return i
        return max_iter


    def get_color(self, z: complex, max_iter: int = 100) -> tuple:
        if z < max_iter:
            return (int(z/max_iter*255)%255, 0, int(z * 255 / max_iter)%255)
        elif z == max_iter:
            return (255, 255, 255)
        else:
            return (0, 0, 0)
            
        
    def get_mandelbrot_zoom(self, img, x_range, y_range, max_iter=1000):
        '''
        creates a mandelbrot set with a zoom
        :param img: the image to draw on
        :param x_range: the range of the x axis
        :param y_range: the range of the y axis
        :param max_iter: the maximum number of iterations'''
        draw = ImageDraw.Draw(img)
        for x in tqdm(range(dimx)):
            cx = x/dimx*(x_range[1]-x_range[0])+x_range[0]
            for y in range(dimy):
                cy = y/dimy*(y_range[1]-y_range[0])+y_range[0]
                c = complex(cx, cy)
                z = self.get_z(c, max_iter=max_iter)
                color = self.get_color(z, max_iter=max_iter)
                draw.point((x, y), fill=color)
        return img

        
    def get_mandelbrot(self, dimx: int, dimy: int, max_iter: int = 100) -> Image:
        img = Image.new('RGB', (dimx, dimy))
        draw = ImageDraw.Draw(img)
        for x in range(dimx):
            for y in range(dimy):
                c = complex(x/dimx*3-2, y/dimy*3-1.5)
                z = self.get_z(c, max_iter=max_iter)
                color = self.get_color(z, max_iter=max_iter)
                draw.point((x, y), fill=color)
        return img


class CircleFractal():
    '''
    creates a circle fractal using inversion geometry
    :param num_main_circles: the number of main circles that will be used to create the fractal
    :param main_circle_radius: the radius of the main circles
    :param min_radius: the minimum radius of the circles in the fractal
    :param max_depth: the maximum depth of the fractal
    :param prints: if true, prints data to the terminal
    '''
    
    center_angle: float
    center_distance: float
    main_circle_radius: float
    outer_circle_radius: float
    inverse_circle_radius: float
    tiny_inverse_circle_radius: float
    num_main_circles: int
    plots: list[tuple[tuple[int, int], int]]
    
    def __init__(self, num_main_circles, main_circle_radius, min_radius, max_depth, prints=False):
        self.num_main_circles = num_main_circles
        self.main_circle_radius = main_circle_radius
        self.max_depth = max_depth
        self.min_radius = min_radius
        self.prints = prints
        self.main_circles = self.create_main_circles(self.num_main_circles, self.main_circle_radius)
        self.inverse_circles = self.create_inverse_circles(self.main_circles)
        # print('inverse circles', self.inverse_circles)
        self.plots = self.generate_fractal(self.max_depth)

    def circle_inversion(self, original_circle: tuple[tuple[int, int], int], inversion_circle: tuple[tuple[int, int], int]):
        '''
        inverts a circle around another circle.
        :param original_circle: the circle to be inverted
        :param inversion_circle: the circle that the original circle will be inverted around
        :return: the inverted circle'''
        
        # x and y coordinates of the center of the circle that will invert the original circle
        
        inversion_center, inversion_circle_radius = inversion_circle
        
        inversion_circle_x, inversion_circle_y = inversion_center
        
        original_center, original_radius = original_circle
        # x and y coordinates of the center of the circle to be inverted
        original_x, original_y = original_center
        
        # distance between the center of the original circle and the center of the inversion circle
        x_distance = original_x - inversion_circle_x
        y_distance = original_y - inversion_circle_y
        
        # pythagoras theorem
        pythagoras = (x_distance ** 2) + (y_distance ** 2)
        
        # scale factor for the inversion
        scale = (inversion_circle_radius ** 2) / (pythagoras - (original_radius ** 2))
        
        
        # inverted center 
        # it works by scaling the distance between the center of the original circle and the center of the inversion circle
        # the scale is found by dividing the square of the inversion circle radius by the difference between the square of the distance between the two circles and the square of the original circle radius
        inverted_center:tuple[int,int] = (
            inversion_circle_x + (scale * x_distance),
            inversion_circle_y + (scale * y_distance)
        )
        
        # inverted radius
        inverted_radius:int = abs(scale) * original_radius
        
        return inverted_center, inverted_radius
        
    def get_distance(self, point1: tuple[int, int], point2: tuple[int, int]):
        '''
        returns the distance between two points
        '''
        x1, y1 = point1
        x2, y2 = point2
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
    def position_point(self, scale, angle):
        '''
        returns the x and y coordinates of a point on a circle based on the angle and scale
        '''
        x = scale * math.cos(math.radians(angle))
        y = scale * math.sin(math.radians(angle))
        return x, y
        
    def create_main_circles(self, num_main_circles, radius):
        '''
        creates the main circles that will be used to create the fractal
        :param num_main_circles: the number of main circles that will be used to create the fractal
        :param radius: the radius of the main circles
        :return: a list of tuples containing the center point and the radius of the main circles'''
        num_circles = num_main_circles
        self.main_circle_radius = radius
        # create points for the main circles that touch all other circles
        # the center point is (0,0)
        # circles must be equidistant from the center point, but not overlapping each other
        
        sum_interior_angles = (num_circles - 2) * 180
        
        if num_main_circles == 1:
            return [((0,0), radius * 2)]
        elif num_main_circles == 2:
            self.outer_circle_radius = radius * 2
            self.center_distance = radius * 2
            self.center_angle = 180
            return [((-radius, 0), radius), ((radius, 0), radius), ((0,0), radius * 2)]
        
        # the angle between each circle is the sum of the interior angles divided by the number of circles
        angle_between_circles = sum_interior_angles / num_circles
        
        self.center_angle = 180 - angle_between_circles
        
        # the distance between the center point and all of the main circle points
        self.center_distance = radius * 2 * math.sin(math.radians(angle_between_circles / 2)) / math.sin(math.radians(self.center_angle))
        
        if self.prints: print(self.center_distance)
        
        main_circle_centers = []
        starting_angle = 0
        # create the main circle points
        for _ in range(num_circles):
            # x = self.center_distance * math.cos(math.radians(starting_angle))
            # y = self.center_distance * math.sin(math.radians(starting_angle))
            x, y = self.position_point(self.center_distance, starting_angle)
            main_circle_centers.append((x, y))
            # add the angle between each circle from the center point
            starting_angle += self.center_angle
            
        self.outer_circle_radius = self.center_distance + radius
        
        main_circles = []
        for center in main_circle_centers:
            main_circles.append((center, radius))
            
        main_circles.append(((0,0), self.outer_circle_radius))

        if self.prints: print('main circles', main_circles)
        return main_circles 
    
    def create_inverse_circles(self, main_circles: list[tuple[tuple[int, int], int]]):
        '''
        creates the inverse circles that will be used to invert the main circles
        uses the main circles to find the radius of the inverse circles
        :param main_circles: the main circles that will be inverted
        :return: a list of tuples containing the center point and the radius of the inverse circles'''
        inner_POI = []
        main_circles_no_outer_circle = main_circles.copy()
        # remove the outer circle from the list of main circles
        main_circles_no_outer_circle.remove(((0,0), self.outer_circle_radius))
        
        # find the point of intersection between each circle and the next circle
        for i, circle in enumerate(main_circles_no_outer_circle):
            center, radius = circle
            cx, cy = center
            
            next_circle = main_circles_no_outer_circle[(i+1)%len(main_circles_no_outer_circle)]
            next_center, next_radius = next_circle
            nx, ny = next_center
                
            # print(i,'comparing', circle, 'and', next_circle)
            # find the point of intersection between the two circles
            # to simplify the math, we can average the center points of the two circles
            ix = (cx + nx) / 2
            iy = (cy + ny) / 2
            inner_POI.append((ix, iy))
            
        # return inner_POI
        inverse_circles = []
        
        # find the radius of the inside circle
        self.tiny_inverse_circle_radius = self.get_distance((0,0), inner_POI[0])
        # finding outer POI
        outer_POI = []
        starting_angle = 0
        for _ in range(len(main_circles_no_outer_circle)):
            # x = (self.center_distance + radius) * math.cos(math.radians(starting_angle))
            # y = (self.center_distance + radius) * math.sin(math.radians(starting_angle))
            x, y = self.position_point(self.center_distance + radius, starting_angle)
            outer_POI.append((x, y))
            # add the angle between each circle from the center point
            starting_angle += self.center_angle
        
        # return inner_POI, outer_POI
    
        def get_radius_from_segment(inner_point: tuple[int, int], outer_points: list[tuple[int, int]]):
            '''
            returns the radius of the circle that is tangent to the inner point and the outer points
            '''
            # use the outer points for the width of the segment
            width = math.sqrt((outer_points[0][0] - outer_points[1][0])**2 + (outer_points[0][1] - outer_points[1][1])**2)
            # use an outer point and the inner point to find the hypotenuse of the triangle, witch can be used to find the height of the segment
            hypotenuse = math.sqrt((outer_points[0][0] - inner_point[0])**2 + (outer_points[0][1] - inner_point[1])**2)
            if self.prints: print(width, hypotenuse)
            height = math.sqrt((hypotenuse**2) - ((width/2)**2))
            
            # radius segment formula
            radius = (height / 2) + (width**2 / (8 * height))
            
            return radius
        
        
        
        starting_angle = self.center_angle / 2
        for i, inner_point in enumerate(inner_POI):
            outer_points = [outer_POI[i%len(outer_POI)], outer_POI[(i+1)%len(outer_POI)]]
            radius = get_radius_from_segment(inner_point, outer_points)
            self.inverse_circle_radius = radius
            inner_p_distance = self.get_distance((0,0), inner_point)
            x, y = self.position_point(radius + inner_p_distance, starting_angle)
            inverse_circles.append(((x, y), radius))
            starting_angle += self.center_angle
            
        # add the tiny circle in the center
        inverse_circles.append(((0,0), self.tiny_inverse_circle_radius))
        
        # self.inverse_circles = inverse_circles
        
        return inverse_circles
            
    def _inversion_fractal(self, circle: tuple[tuple[int, int], int], depth: int):
        '''
        recursively creates the fractal
        :param circle: the circle to be inverted'''
        if depth == 0:
            return []
        
        center, radius = circle
        
        all_points = []
        for inverse_circle in self.inverse_circles:
            inverted_circle = self.circle_inversion(circle, inverse_circle)
            
            # if the inverted circle has a smaller radius than the previous circle, then it is a valid circle
            c, r = inverted_circle
            if r < radius and r > self.min_radius:
                all_points = all_points + [inverted_circle] + self._inversion_fractal(inverted_circle, depth - 1)
            else:
                continue
        
        return all_points
        
    def generate_single_fractal(self, original_circle: tuple[tuple[int, int], int], original_inverse_circle:tuple[tuple[int, int], int], depth: int):
        '''
        generates a new fractal trail
        '''
        new_circle = self.circle_inversion(original_circle, original_inverse_circle)
        
        plots = []
        
        plots.append(new_circle)
        
        plots += self._inversion_fractal(new_circle, depth)
        
        return plots
    
    def generate_fractal(self, depth: int):
        '''
        generates the total fractal'''
        plots = []
        
        for circle in tqdm(self.main_circles):
            # find the inverse circle that is farthest away from the main circle
            inverse_circle = max(self.inverse_circles, key=lambda x: self.get_distance(circle[0], x[0]))
            if self.prints: print('farthest inverse circle', inverse_circle)
            
            center, radius = circle
            if center == (0,0):
                inverse_circle = self.inverse_circles[-1]
            
            plots += self.generate_single_fractal(circle, inverse_circle, depth)
            
        # print(plots)
        return plots
        
    def get_color(self, plot: tuple[tuple[int,int],int]):
        # get the color of the circle based on the radius and position
        center, radius = plot
        x, y = center
        return (int(x) % 255, int(y) % 255, int(radius) % 255)
        
    def draw_plots(self, img: Image, offset: (int, int) = (0,0)):
        '''
        draws the plots on the image
        '''
        draw = ImageDraw.Draw(img)
        
        for plot in self.plots:
            center, radius = plot
            x, y = center
            # offset the center point to the center of the image
            x += dimx / 2 + offset[0]
            y += dimy / 2 + offset[1]
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=self.get_color(plot), outline='black')
            
            

tri = CircleFractal(3, 300, 1, 40)
quad = CircleFractal(4, 900, 1, 40)
# mandel = Mandelbrot()

img = Image.new('RGB', (dimx, dimy), color = 'white')
img2 = Image.new('RGB', (dimx, dimy), color = 'white')
img3 = Image.new('RGB', (dimx, dimy), color = 'white')
tri.draw_plots(img)
quad.draw_plots(img2)
# mandel.get_mandelbrot_zoom(img3, (-2, 2), (-2, 2), max_iter=100)
img.show()
img2.show()
# img3.show()

