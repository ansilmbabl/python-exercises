#turtle sherin

import turtle as t

t.speed(10)
t.color("red")
t.pensize(6)

for i in range(24):
    for j in range(4):
        t.forward(200)
        t.left(90)
    t.left(15)
t.mainloop()
