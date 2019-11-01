#Created By Piyush Mishra
import random
import turtle 
import sys
def createA():
	a = turtle.Turtle()
	
	a.write("HANGMAN!!", font=("Arial", 30, "normal"))
	#turtle.mainloop()
		
def createDash(num):
	dash=[]
	letter=[]
	for i in range(num):
		dash.append(turtle.Turtle())
		letter.append(turtle.Turtle())		
		dash[i].ht()
		letter[i].ht()		
		dash[i].penup()
		letter[i].penup()		
		dash[i].setpos(i*100,-200)
		letter[i].setpos(i*100,-200)		
		dash[i].pendown()
		letter[i].pendown()
		dash[i].fd(50)
		dash[i].lt(90)
	#turtle.mainloop()
	return letter
#i = input()		
		
f = open("movies.txt")
f = f.read().split()

r = random.choice(f)
l = len(r)
movie_list = r.split()
user_list  = []
user_input=[]
for i in range(len(movie_list)):
	user_list.append('__')
print("Enter a character")
letter = createDash(7)
createA()
me="Piyush"
for i in range(7):
	letter[i].write(input(), align="right",font = ("Arial",30,"normal"))

letter[3].ht()
turtle.mainloop()
