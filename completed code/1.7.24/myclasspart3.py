#Encapsulation
#Encapsulate the properties inside the class
# in other language program keyword like: 
# - public
# - private
# - protected

class circle:

    def __init__ (self, radius):
        #change the property with single underscore
        #this make the property private
        self.radius = 0
        if (isinstance(radius, int)):
            self.radius = radius
        else:
            print("Invalid Radius")

    # getter method and setter method

    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        if (isinstance(radius, int)):
            self.radius = radius
        else:
            print("Invalid Radius")

    # property is a class
    # we are calling/invoking the class by passing the method as argument
    # please notice after getRadius there is no ()
    # the property class returns the property object which is assigned to
    # a variable radius
    # in other words radius is an instance of property class

    radius = property(getRadius, setRadius)

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"Radius of this circle is {self.radius}"











mycircle = circle(20)
print(mycircle)
mycircle.radius = 30
#you are indirectly passing the value 30 to the setter method

mycircle.radius = "abc" #test the if condition
print(mycircle.area())
print(mycircle)
#mycircle = circle("abc")
#print(mycircle)



