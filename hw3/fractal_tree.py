import matplotlib
from matplotlib import collections


# vertices = []
# seg = []
#
#
# def produce_vertices(angle, length_ratio):
#     pass
#
#
# def distance(point1, point2):
#     pass
#
#
# lines = [[tuple(vertices[j]) for j in i]for i in segs]
#
# lc = matplotlib.collections.LineCollection(lines)
#
#
#
# class FractalTree(dist_ratio, angle):
#
#
#
#     def __init__(self):
#         self.ratio = dist_ratio
#         self.angle = angle
#
#     def print_tree(self, iterations):
#
#

# Importing the python libraries
import pygame, math

# Initialize all imported pygame modules
pygame.init()

# Create a new surface and window.
surface_height, surface_width = 1800, 1800  # Surface variables
main_surface = pygame.display.set_mode((surface_height, surface_width))

# Captioning the window
pygame.display.set_caption("Fractal_Tree")


def draw_tree(order, theta_r, theta_l, sz, posn, heading, color=(0, 0, 0), depth=0):
    # The relative ratio of the trunk to the whole tree
    trunk_ratio_r = 1 - .65
    trunk_ratio_l = 1 - .7


    # Length of the trunk
    trunk = sz * (min(trunk_ratio_l, trunk_ratio_r))
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = posn
    newpos = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, posn, newpos)

    if order > 0:  # Draw another layer of subtrees

        # These next six lines are a simple hack to make
        # the two major halves of the recursion different
        # colors. Fiddle here to change colors at other
        # depths, or when depth is even, or odd, etc.
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

            # make the recursive calls to draw the two subtrees
        newsz_r = sz * (1 - trunk_ratio_r)
        newsz_l = sz * (1- trunk_ratio_l)
        draw_tree(order - 1, theta_r, theta_l, newsz_r, newpos, heading - theta_r, color, depth + 1)
        draw_tree(order - 1, theta_r, theta_l, newsz_l, newpos, heading + theta_l, color, depth + 1)


def main():
    inst_name = 'mixed_c_60_40_70_65'
    theta_r = math.pi/180 * 40
    theta_l = math.pi / 180 * 60

    # This little part lets us draw the stuffs
    # in the screen everything
    main_surface.fill((255, 255, 255))
    draw_tree(13, theta_r, theta_l, surface_height * 0.9, (surface_width // 2 - 100, surface_width - 50), -math.pi / 2)
    pygame.display.flip()
    pygame.image.save(main_surface, inst_name + "_tree.png")

    # Calling the main function


main()
#it()
