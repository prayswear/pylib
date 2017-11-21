import turtle
turtle.setup(800,600,0,0,)
turtle.pensize(1)
turtle.speed(100)
turtle.color("red")
turtle.shape("turtle")
a=input("请输入任意1-10以内的数值：")
a=eval(a)
for i in range(5):
   a=a+10
   turtle.left(90)
   turtle.fd(a)
turtle.done()

