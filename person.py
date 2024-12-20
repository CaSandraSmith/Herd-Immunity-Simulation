import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        # TODO Define the other attributes of a person here
        self.is_alive = True
        self.is_vaccinated = is_vaccinated
        self.infection = infection

    def did_survive_infection(self, virus):
        # This method checks if a person survived an infection. 
        # TODO Only called if infection attribute is not None.
        if self.infection == None: return
        
        # Check generate a random number between 0.0 - 1.0
        random_number = random.random()
        
        # If the number is less than the mortality rate of the 
        if random_number < virus.mortality_rate:
            # person's infection they have passed away. 
            self.infection = False
            self.is_alive = False
            return False
        # Otherwise they have survived infection and they are now vaccinated. 
        else:
            # Set their properties to show this
            self.is_vaccinated = True
            self.infection = False
            return True
        # TODO: The method Should return a Boolean showing if they survived.

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class

    # Test 1
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Test 2
    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None
    
    # Test 3
    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert isinstance(infected_person.infection, Virus)
    
    # Test 4
    vaccinated_person2 = Person(4, True)
    assert vaccinated_person2._id == 4
    assert vaccinated_person2.is_alive is True
    assert vaccinated_person2.is_vaccinated is True
    assert vaccinated_person2.infection is None
    
    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 101):
        # TODO Make a person with an infection
        # TODO Append the person to the people list
        new_person = Person(i, False, virus)
        people.append(new_person)
        

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 

    # Count the people that survived and did not survive: 
   
    did_survived = 0
    did_not_survive = 0

    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive
    
    for person in people:
        # For each person call that person's did_survive_infection method
        survived = person.did_survive_infection(virus)
        
        if survived: did_survived += 1
        else: did_not_survive += 1

    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 
    print(f"{did_survived} people survived.")
    print(f"{did_not_survive} people didn't survive.")


    # Stretch challenge! 
    
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    unInfected_people = []
    for i in range(1, 101):
        new_person = Person(i, False)
        
        # Generate a random number. If that number is less than the 
        random_number = random.random()

        if random_number < virus.repro_rate:
            # infection rate of the virus that person is now infected. 
            # Assign the virus to that person's infection attribute. 
            new_person.infection = virus
        
        unInfected_people.append(new_person)
        
    is_infected = 0
    is_not_infected = 0
    
    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.
    for person in unInfected_people:
        if person.infection == None:
            is_not_infected += 1
        else:
            is_infected += 1
    
    print(f"{is_infected} people were infected.")
    print(f"{is_not_infected} people weren't infected.") 
    
        