import turtle as t

#for x in range(3):
#    t.forward(100)
#    t.left(120)
#
#t.penup()
#t.forward(200)
#t.pendown()
#t.dot(10, "red")
#t.color("blue")
#t.forward(50)

#t.mainloop()

# 1. Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.


def turtle_kvadrat(range_side):
    for x in range(4):
        t.forward(range_side)
        t.left(90)


def turtle_move_pen(range_move):
    t.penup()
    t.forward(range_move)
    t.pendown()


def turtle_pen_color(color):
    t.color(color)


def turtle_poc(range_fd, range_s, color, antal):
    t.hideturtle()
    for x in range(antal):
        turtle_pen_color(color)
        turtle_kvadrat(range_s)
        turtle_move_pen(range_fd)


def turtle_circle(loops, forward, angle, color):
    for x in range(loops):
        t.color(color)
        t.forward(forward)
        t.right(angle)


def turtle_text(color):
    t.color(color)
    t.pensize(5)


    def turtle_text_stort_p():
        t.left(90)
        t.forward(100)
        t.right(90)
        t.circle(-25, 180)
        t.left(90)
        t.forward(50)
        t.left(90)
        turtle_move_pen(60)


    def turtle_text_litet_y():
        t.left(70)
        t.forward(55)
        t.left(180)
        t.forward(25)
        t.right(125)
        t.forward(25)
        t.right(125)
        turtle_move_pen(60)


    def turtle_text_litet_t():
        t.right(90)
        t.forward(50)
        t.right(180)
        turtle_move_pen(30)
        t.right(90)
        t.backward(8)
        t.forward(16)
        turtle_move_pen(30)


    def turtle_text_litet_h():
        t.left(90)
        turtle_move_pen(20)
        t.right(180)
        t.forward(50)
        t.left(180)
        t.forward(15)
        t.circle(-15, 180)
        t.forward(15)


    def turtle_text_litet_o():
        t.left(90)
        turtle_move_pen(35)
        t.circle(15, 360)


    def turtle_text_litet_n():
        turtle_move_pen(35)
        t.left(90)
        t.forward(30)
        t.right(180)
        t.forward(15)
        t.left(180)
        t.circle(-15, 180)
        t.forward(15)

    turtle_text_stort_p()
    turtle_text_litet_y()
    turtle_text_litet_t()
    turtle_text_litet_h()
    turtle_text_litet_o()
    turtle_text_litet_n()
