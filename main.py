import colorgram
import turtle as turtle_module
import random


# colors = colorgram.extract("image.jpg", 10)
#
# color_list = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_tuple = (red, green, blue)
#     color_list.append(color_tuple)
#
# print(color_list)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(235, 246, 250), (251, 241, 246), (245, 252, 249), (243, 235, 74), (211, 158, 93),
              (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# tim.pensize(20)
# tim.speed(10)
#
# for x in range(0,10):
#     for y in range(0, 10):
#         tim.color(random.choice(new_colors))
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()
#         tim.forward(50)
#     tim.left(90)
#     tim.forward(50)
#     tim.left(90)
#     tim.forward(600)
#     tim.right(180)

#10 by 10 spots
#20 dot size, 50 spaces

screen = turtle_module.Screen()
screen.exitonclick()