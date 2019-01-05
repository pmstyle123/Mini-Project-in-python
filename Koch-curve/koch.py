#ASSIGNMENT - 4  by Piyush Mishra
#New functions learned from https://docs.python.org/3.4/library/turtle.html

import turtle
bob = turtle.Turtle()
bob2 = turtle.Turtle()
bob3=turtle.Turtle()
bob4=turtle.Turtle()
bob5 = turtle.Turtle()
bob6=turtle.Turtle()
bob7=turtle.Turtle()
bob8=turtle.Turtle()
bobc=turtle.Turtle()

bob.color("#CE1313")
bob2.color("#CE1313")
bob3.color("#CE1313")
bob4.color("#CE1313")
bob5.color("#CE1313")
bob6.color("#CE1313")
bob7.color("#CE1313")
bob8.color("#CE1313")




def edge(t,edgelen,n):
	if(n==1):
		t.fd(edgelen)
	else :
		elen =int(edgelen/3)
		edge(t,elen,n-1)
		t.lt(60)
		edge(t,elen,n-1)
		t.rt(120)
		edge(t,elen,n-1)
		t.lt(60)
		edge(t,elen,n-1)
		
		
bob.penup()
bob.setpos(-600,0)
bob.pendown()

			
bob.begin_fill()			
edge(bob,300,4)
bob.end_fill()

x = bob.xcor()

bob2.penup()
bob2.setpos(x,0)
bob2.lt(180)
bob2.pendown()

bob2.begin_fill()
edge(bob2,300,4)
bob2.end_fill()


bob3.penup()
bob4.penup()
bob5.penup()
bob6.penup()
bob7.penup()
bob8.penup()

bob3.setpos(x,0)
bob3.pendown()
bob3.begin_fill()
edge(bob3,300,4)
bob3.end_fill()


x3=bob3.xcor()


bob5.setpos(x,0)
bob5.lt(90)
bob5.pendown()
bob5.begin_fill()
edge(bob5,300,4)
bob5.end_fill()


x5=bob5.ycor()


bob7.setpos(x,0)
bob7.rt(90)
bob7.pendown()
bob7.begin_fill()
edge(bob7,300,4)
bob7.end_fill()
x7=bob7.ycor()
bob4.setpos(x3,0)
bob4.lt(180)
bob4.pendown()
bob4.begin_fill()
edge(bob4,300,4)
bob4.end_fill()
bob6.setpos(x,x5)
bob6.rt(90)
bob6.pendown()
bob6.begin_fill()
edge(bob6,300,4)
bob6.end_fill()
bob8.setpos(x,x7)
bob8.lt(90)
bob8.pendown()
bob8.begin_fill()
edge(bob8,300,4)
bob8.end_fill()


bobc.penup()
bobc.setpos(bob3.xcor(),0)
bobc.lt(90)
bobc.pendown()
bobc.pensize(20)
bobc.circle(bob3.xcor()-bob.xcor())

turtle.mainloop()


			
			
