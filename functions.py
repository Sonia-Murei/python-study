def hello(name):
    return f'Hello {name}'

name1=hello('Sonia')
print(name1)
name2=hello('Kyle')
print(name2)
name3=hello('Njeri')
print(name3)

def triangle_area(base,height):
    area=0.5*base*height
    return area

triangle1=triangle_area(20,30)
print(triangle1)
triangle2=triangle_area(50,40)
print(triangle2)
triangle3=triangle_area(150,80)
print(triangle3)

# Create a function that calculates the area of a circle
def circle_area(radius):
    area=3.14*radius**2
    return area

circle1=circle_area(21)
print(circle1)
circle2=circle_area(135)
print(circle2)
circle3=circle_area(70)
print(circle3)

# Create a function that calculates the area of a rectangle

def rectangle_area(length,width):
    area=length*width
    return area

rectangle1=rectangle_area(30,15)
print(rectangle1)
rectangle2=rectangle_area(50,25)
print(rectangle2)
rectangle3=rectangle_area(60,20)
print(rectangle3)

# Create a function that checks if a number is even or odd:

def even_odd(num):
    if num%2==0:
        res='Even'
    else:
        res='Odd'
    return res
    
num1=even_odd(20)
print(num1)
num2=even_odd(35)
print(num2)