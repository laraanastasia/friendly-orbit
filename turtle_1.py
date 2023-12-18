import turtle
t = turtle.Turtle() 

  
c = t.clone()  
d=t.clone()
t.color("blue") 
t.speed(0)
c.color("red") 
c.speed(0) 
d.color("green")
d.speed(0)
for i in range(50,600,5):
    t.circle(i) 
 
for i in range(50, 600, 10):  
    c.circle(i)  
  
for i in range(50,600,8):
    d.circle(i)
turtle.mainloop()  