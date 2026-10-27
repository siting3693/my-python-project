#OOP
class Person:
  species = "Human"               #Class property
  def __init__(self, name, age=18):     #self is required for python to send name of object to here (eg. p1)  #age = 18 default value
    self.name = name              #Object property (instance property)
    self.age = age                      #left side self.name is actually p1.name of attribute (eg.) while right side name is value get from the parameter name

  def greet(self):
    return "Hello, " + self.name   #although here need to use name, we dont need name as parameter (need self only)

  def welcome(self):
    message = self.greet()              #call another function in a function using self.function()
    print(message + "! Welcome to our website.")


p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
p1.welcome()         #call function using self.function()

p1.age = 26             #modify object property
Person.species = "Good" #modify class property

del p1.age            #delete property
print(p1.name)        #This works
# print(p1.age)       #This would cause an error

del Person.welcome

p1.city = "Oslo"      #add new property to this object only

print(p1.name, p1.city)
print(p2.name, p2.age)

print(p1.species)     #same class property
print(p2.species)

#The self parameter must be the first parameter of any method in the class.
#self can be any other name, just that there should be a parameter before any other parameter, but strongly recommend use self


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")      #use self.attributename (attribute same as property)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()



class Calculator:
  def add(self, a, b):
    return a + b
calc = Calculator()
print(calc.add(5, 3))    #can use function normally




class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1                    #can modify in class
    print(f"Happy birthday! You are now {self.age}")

p1 = Person2("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()



#__str__
print(p1)    #without __str__

class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"     #with __str__, can control what is returned when the object is printed

p1 = Person3("Tobias", 36)
print(p1)






class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []              #all objects have empty songs list at first, no need parameter

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()




#INHERITANCE
class Student(Person):     #create child class(derived class) from parent class(base class), class child(parent):
  pass

x = Student("Mike", 16)
print(x.greet())




class Person:   #parent
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):   #child
  def __init__(self, fname, lname):    #The child's __init__() function overrides the inheritance of the parent one (to add property of object to student)
    Person.__init__(self, fname, lname)   #To keep the inheritance of the parent's __init__() function

class Student(Person):
  def __init__(self, fname, lname, year):    #add new parameter for new property
    super().__init__(fname, lname)       #Person. or super().
    self.graduationyear = year           #add new property

  def welcome(self):                    #add new function
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)




#POLYMORPHISM
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):     #override the move() method
    print("Sail!")

class Plane(Vehicle):
  def move(self):     #override the move() method
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()       #execute the same method for three classes




#ENCAPSULATION
class Person:
  def __init__(self, name, age, salary):
    self.name = name
    self.__age = age         #Private property: add double underscore prefix
    self._salary = salary    #Protected property: add single underscore prefix (like putting a "Staff Only" sign on an unlocked door)

  def get_age(self):         #add a get method to access a private property
    return self.__age

  def set_age(self, age):    #add a set method to modify a private property
    if age > 0:              #can validate data before setting it
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Emil", 25, 12000)
print(p1.name)

#print(p1.__age)            This will cause an error (private property)
print(p1.get_age())
print(p1._Person__age)      #Name Mangling: add _class__ can access private property but not recommend because It defeats the purpose of encapsulation

p1.set_age(26)
print(p1.get_age())

print(p1._salary)           #Can access, but shouldn't



#
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):      #private method: can only be used by other methods inside the class, cannot be called directly from outside the class
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
print(calc._Calculator__validate(5))   #Name Mangling, not recommend










#INNER CLASSES
class Computer:
    def __init__(self, brand):
        self.brand = brand
        # List to hold our complex RAM objects
        self.ram_sticks = []          #because it's one-to-many relationship, so we slowly add on the RAM sticks on each computer afterwards

    def add_ram(self, size, speed, gen, brand):
        # 1. Use the inner blueprint to build a detailed RAM object
        new_ram = self.RAM(size, speed, gen, brand)       #create a new object under RAM class
        
        # 2. Add this new object to the computer's list
        self.ram_sticks.append(new_ram)
        print(f"Added: {brand} {size}GB {gen} ({speed}MHz) stick.")

    def show_system_specs(self):
        # Calculate total RAM by looping through the objects
        total_gb = sum(stick.size for stick in self.ram_sticks)    #stick is just x like for x in range(5)    ram_sticks is one of the properties of Computer while size is one of the properties of RAM

        #SAME AS
        #for x in self.ram_sticks  (self.ram_sticks is a list of RAM objects)
            #total_gb = total_gb + x.size    (add the size of each RAM objects)
        
        print(f"\n--- {self.brand} System Specs ---")
        print(f"Total Memory: {total_gb}GB")
        print("Installed Modules:")
        
        # Loop through each RAM object to print its specific properties
        for i, stick in enumerate(self.ram_sticks, 1):          #count i for self.ram_sticks starts from 1
            print(f"  Slot {i}: {stick.brand} {stick.size}GB {stick.gen} @ {stick.speed}MHz")
    
    def run_memory_diagnostics(self):
        print("\nRunning Memory Diagnostics...")
        # The computer tells each RAM stick to test itself
        for stick in self.ram_sticks:
            stick.run_diagnostics()     #each RAM object run this inner function

    # --- THE INNER CLASS ---
    class RAM:
        def __init__(self, size, speed, gen, brand):
            # Now the RAM holds multiple distinct properties
            self.size = size
            self.speed = speed
            self.gen = gen
            self.brand = brand
            
        def run_diagnostics(self):
            # The RAM has its own behavior
            print(f"Testing {self.brand} {self.size}GB {self.gen} module... Status: OK")


# --- USAGE ---

# 1. Create the main outer object
my_pc = Computer("Asus")

# 2. Add multiple RAM sticks with full details
my_pc.add_ram(size=16, speed=3200, gen="DDR4", brand="Corsair")
my_pc.add_ram(size=16, speed=3200, gen="DDR4", brand="Corsair")
my_pc.add_ram(size=32, speed=3600, gen="DDR4", brand="G.Skill")

# 3. View the system specs (Outer class behavior)
my_pc.show_system_specs()

# 4. Trigger the diagnostics (Outer class triggering inner class behavior)
my_pc.run_memory_diagnostics()






class Computer:
    # 1. We add parameters for the CPU details right here in the main blueprint
    def __init__(self, brand, cpu_name, cpu_speed):
        self.brand = brand
        
        # 2. We pass the variables down to the inner class
        self.cpu = self.CPU(cpu_name, cpu_speed)    #Create new CPU object

    def show_specs(self):
        print(f"Computer: {self.brand}")
        self.cpu.display_cpu()           #.cpu refers to the attribute of Computer object (4 lines before)
        print("-" * 20)

    # --- THE INNER CLASS ---
    class CPU:
        def __init__(self, cpu_brand, speed):
            self.cpu_brand = cpu_brand
            self.speed = speed

        def display_cpu(self):
            print(f"CPU: {self.cpu_brand} running at {self.speed}")


# Now we can build computers with totally different CPUs!

# PC 1 gets an Intel processor
my_pc = Computer("Dell", "Intel Core i7", "2.8 GHz")

# PC 2 gets an AMD processor
gaming_pc = Computer("Alienware", "AMD Ryzen 9", "4.5 GHz")

# PC 3 gets an Apple processor
macbook = Computer("Apple", "M2 Max", "3.5 GHz")


my_pc.show_specs()
gaming_pc.show_specs()
macbook.show_specs()
