# circle fractal
import math
import random
from PIL import Image, ImageDraw
from tqdm import tqdm

num_main_circles = 3
main_circle_radius = 100
max_depth = 20
dimx = 1000
dimy = 1000

class CircleFractal():
    
    center_angle: float
    center_distance: float
    main_circle_radius: float
    outer_circle_radius: float
    inverse_circle_radius: float
    tiny_inverse_circle_radius: float
    num_main_circles: int
    plots: list[tuple[tuple[int, int], int]]
    
    def __init__(self, num_main_circles, main_circle_radius, min_radius, max_depth):
        self.num_main_circles = num_main_circles
        self.main_circle_radius = main_circle_radius
        self.max_depth = max_depth
        self.min_radius = min_radius
        self.main_circles = self.create_main_circles(self.num_main_circles, self.main_circle_radius)
        self.inverse_circles = self.create_inverse_circles(self.main_circles)
        print('inverse circles', self.inverse_circles)
        self.generate_fractal(self.max_depth)

    def circle_inversion(self, original_circle: tuple[tuple[int, int], int], inversion_circle: tuple[tuple[int, int], int]):
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
        x1, y1 = point1
        x2, y2 = point2
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
    def position_point(self, scale, angle):
        x = scale * math.cos(math.radians(angle))
        y = scale * math.sin(math.radians(angle))
        return x, y
        
    def create_main_circles(self, num_main_circles, radius):
        
        num_circles = num_main_circles
        self.main_circle_radius = radius
        # create points for the main circles that touch all other circles
        # the center point is (0,0)
        # circles must be equidistant from the center point, but not overlapping each other
        
        sum_interior_angles = (num_circles - 2) * 180
        
        if num_main_circles == 1:
            return [(0,0)]
        elif num_main_circles == 2:
            return [(-radius, 0), (radius, 0)]
        
        # the angle between each circle is the sum of the interior angles divided by the number of circles
        angle_between_circles = sum_interior_angles / num_circles
        
        self.center_angle = 180 - angle_between_circles
        
        # the distance between the center point and all of the main circle points
        self.center_distance = radius * 2 * math.sin(math.radians(angle_between_circles / 2)) / math.sin(math.radians(self.center_angle))
        
        print(self.center_distance)
        
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

        print('main circles', main_circles)
        return main_circles 
    
    def create_inverse_circles(self, main_circles: list[tuple[tuple[int, int], int]]):
        
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
            
            # use the outer points for the width of the segment
            width = math.sqrt((outer_points[0][0] - outer_points[1][0])**2 + (outer_points[0][1] - outer_points[1][1])**2)
            # use an outer point and the inner point to find the hypotenuse of the triangle, witch can be used to find the height of the segment
            hypotenuse = math.sqrt((outer_points[0][0] - inner_point[0])**2 + (outer_points[0][1] - inner_point[1])**2)
            print(width, hypotenuse)
            height = math.sqrt((hypotenuse**2) - ((width/2)**2))
            
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
        
        new_circle = self.circle_inversion(original_circle, original_inverse_circle)
        
        plots = []
        
        plots.append(new_circle)
        
        plots += self._inversion_fractal(new_circle, depth)
        
        return plots
    
    def generate_fractal(self, depth: int):
        
        plots = []
        
        for circle in self.main_circles:
            # find the inverse circle that is farthest away from the main circle
            inverse_circle = max(self.inverse_circles, key=lambda x: self.get_distance(circle[0], x[0]))
            print('farthest inverse circle', inverse_circle)
            
            center, radius = circle
            if center == (0,0):
                inverse_circle = self.inverse_circles[-1]
            
            plots += self.generate_single_fractal(circle, inverse_circle, depth)
            
        print(plots)
        return plots
        
        

CircleFractal(3, 30, .002, 5)
        