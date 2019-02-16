# this file is run before tests to suppress graphics in test suite mode

# suppress matplotlib 
import matplotlib
matplotlib.use('Agg')

# suppress turtle graphics
import turtle
turtle.bye()


