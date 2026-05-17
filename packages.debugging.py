'''Packages & Debugging
    (1)Python packages & core package
    (2)Package menejer & extarnal package
    (3)Debugging
'''
# import turtle
# t = turtle.Turtle()

# t.shape("turtle")
# t.speed(0.5)
# t.circle(100)
# turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()

with open("material/message.txt", "r") as your_file:
    content = your_file.read()
    print("your file:", content)
print("DONE")
